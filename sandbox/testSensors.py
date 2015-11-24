from w1thermsensor import W1ThermSensor

from Adafruit_BME280 import *

sensor = BME280(mode=BME280_OSAMPLE_8)

degrees = sensor.read_temperature()
pascals = sensor.read_pressure()
hectopascals = pascals / 100
humidity = sensor.read_humidity()

temp_sensor = W1ThermSensor()
temperature_in_celsius = temp_sensor.get_temperature()
temperature_in_fahrenheit = temp_sensor.get_temperature(W1ThermSensor.DEGREES_F)
temperature_in_all_units = temp_sensor.get_temperatures([W1ThermSensor.DEGREES_C, W1ThermSensor.DEGREES_F, W1ThermSensor.KELVIN])

while True:
    temperature_in_celsius = temp_sensor.get_temperature()
    print ('Timestamp = {0:0.3f}'.format(sensor.t_fine))
    print ('Temp      = {0:0.3f} deg C'.format(degrees))
    print ('Pressure  = {0:0.2f} hPa'.format(hectopascals))
    print ('Humidity  = {0:0.2f} %'.format(humidity))
    print("water temp = " + temperature_in_celsius)
