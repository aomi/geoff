from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
from probe import retrieve
from datetime import datetime
from math import fabs
from celery import Celery
from peewee import *
import RPi.GPIO as GPIO
import models
import redis
import celeryconfig
import Adafruit_BME280 as BME

# database setup
db = SqliteDatabase('database.db')
db.create_tables([models.Sensor], True)
rdb = redis.StrictRedis(host='localhost', port=6379, db=0)

# celery setup
celery = Celery('tasks')
celery.config_from_object(celeryconfig)

# setup GPIO pins for relays
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

# setup motor hat for steering and winch
mh = Adafruit_MotorHAT(addr=0x60)

steer_motor = mh.getStepper(200, 1)  # 200 steps/rev, motor port #1
winch_motor = mh.getStepper(200, 2)
rdb.set('steer_motor', False)
rdb.set('winch_motor', False)
rdb.set('troll_motor', 'stop')
rdb.set('steer_motor_step', 0)
rdb.set('winch_motor_step', 0)
rdb.set('probe', False)
steer_motor_max = 383
winch_motor_max = 500

steer_motor.setSpeed(30)
winch_motor.setSpeed(30)

# configure temp, pressure, humidity sensor
sensor = BME.BME280(mode=BME.BME280_OSAMPLE_8)


# move motors
@celery.task(name='tasks.move')
def move_motor(select_motor, step, control):
    # check if the motor is in use
    if rdb.get(select_motor) == 'False':
        motor = None
        direction = None
        step_counter = None
        # select which motor to use
        if select_motor == 'steer_motor':
            motor = steer_motor
            step_counter = 'steer_motor_step'
        elif select_motor == 'winch_motor':
            motor = winch_motor
            step_counter = 'winch_motor_step'

        # set direction
        if step > 0:
            direction = Adafruit_MotorHAT.FORWARD
        elif step < 0:
            direction = Adafruit_MotorHAT.BACKWARD

        # set selected motor usage state to true
        rdb.set(select_motor, True)
        if control == 'auto':
            motor.step(int(fabs(step)), direction, Adafruit_MotorHAT.DOUBLE)
            value = int(rdb.get(step_counter)) + int(step)
            rdb.set(step_counter, value)
        elif control == 'manual':
            while True:
                motor.oneStep(direction,Adafruit_MotorHAT.DOUBLE)
                if rdb.get(select_motor) == 'False':
                    break
        rdb.set(select_motor, False)
    else:
        print('motor in use')


# recalibrate motor to a known position
@celery.task(name='reset')
def reset_motor(select_motor):
    if select_motor == 'steer_motor':
        if rdb.get(select_motor) == 'False':
            # run reset instructions
            steer_motor.step(20, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
    elif select_motor == 'winch_motor':
        if rdb.get(select_motor) == 'False':
            # run reset instructions
            winch_motor.step(20, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)


# get sensor data and store it
@celery.task(name='sensor')
def get_sensor_data(select_sensor):
    input_data = None
    sensor_unit = None
    # connect to SQLite file
    db.connect()
    if select_sensor == 'air_temp':
        input_data = sensor.read_temperature()
        sensor_unit = 'celsius'
    elif select_sensor == 'pressure':
        input_data = sensor.read_pressure()
        sensor_unit = 'pascals'
    elif select_sensor == 'humidity':
        input_data = sensor.read_humidity()
        sensor_unit = 'humidity'
    else:
        return 'invalid sensor type'
    # store data of sensor into database.db
    data = models.Sensor(sensor_type=select_sensor, data=input_data, unit=sensor_unit, date=datetime.now())
    # store most recent collected data into redis db
    rdb.set(select_sensor, input_data)
    data.save()
    db.close()
    return input_data


@celery.task(name='probe')
def get_probe_data():
    # probe has it's own function as it can not be ran in parallel
    if rdb.get('probe') == 'False':
        rdb.set('probe', True)
        ph = retrieve('ph')
        water_temp = retrieve('water_temp')
        db.connect()
        ph_data = models.Sensor(sensor_type='ph', data=ph, unit='pH', date=datetime.now())
        water_temp_data = models.Sensor(sensor_type='water_temp', data=water_temp, unit='Celsius', date=datetime.now())
        ph_data.save()
        water_temp_data.save()
        db.close()
        rdb.set('probe', False)
        rdb.set('ph', ph)
        rdb.set('water_temp', water_temp)
        return str(ph), str(water_temp)


# switch motor
@celery.task(name='tasks.troll')
def troll(control):
    # toggling relays
    if control == 'forward':
        GPIO.output(12, False)
        GPIO.output(13, True)
        rdb.set('troll_motor', 'forward')
        return True
    elif control == 'backward':
        GPIO.output(12, True)
        GPIO.output(13, False)
        rdb.set('troll_motor', 'backward')
        return True
    elif control == 'stop':
        GPIO.output(12, False)
        GPIO.output(13, False)
        rdb.set('troll_motor', 'stop')
        return True
    else:
        print('invalid command')
        return False
