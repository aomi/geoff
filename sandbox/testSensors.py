from openpyxl import Workbook
from openpyxl.compat import range
from w1thermsensor import W1ThermSensor
from datetime import datetime
from Adafruit_BME280 import *
import RPi.GPIO as GPIO
import time

#Intializing Workbook
wb = Workbook()
name = raw_input("Name of Document? ")
dest_filename = str(name) + '.xlsx'
ws1 = wb.active
ws1.title = "Sensor Data"

#changing GPIO Modes
GPIO.setmode(GPIO.BCM)

#Analog to digital converter reader
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, True)

        GPIO.output(clockpin, False)  # start clock low
        GPIO.output(cspin, False)     # bring CS low

        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(mosipin, True)
                else:
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)

        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1

        GPIO.output(cspin, True)
        
        adcout >>= 1       # first bit is 'null' so drop it
        return adcout

#Initalizing Sensor/Pin Variables
bme_sensor = BME280(mode=BME280_OSAMPLE_8)
water_temp_sensor = W1ThermSensor()
SPICLK = 18
SPIMISO = 23
SPIMOSI = 24
SPICS = 25
ph_sensor_pin = 0;

#Setup GPIO Pins
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)


#Variables for get_ph function
last_read = 0       # this keeps track of the last ph value
tolerance = 3       # to keep from being jittery we'll only change every 3 units

def get_ph(last_value):
        ph_value = readadc(ph_sensor_pin, SPICLK, SPIMOSI, SPIMISO, SPICS)
        # how much has it changed since the last read?
        ph_adjust = abs(ph_value - last_value)

        if (ph_adjust > tolerance):
                # save the ph reading for the next test
                last_read = ph_value
                return 18.7-3*ph_value/200

ws1['A1'] = "Time"
ws1['B1'] = "Air_Temp (C)"
ws1['C1'] = "Pressure (hPa)"
ws1['D1'] = "Humidity (%)"
ws1['E1'] = "Water_Temp (C)"
ws1['F1'] = "Water pH (ph)"
row = 1

try:
    while True:
        
        air_temp     = bme_sensor.read_temperature()
        pascals      = bme_sensor.read_pressure()
        hectopascals = pascals / 100
        humidity     = bme_sensor.read_humidity()
        water_temp   = water_temp_sensor.get_temperature()
        ph           = get_ph(last_read)
        time         = datetime.now()
        
        ws1['A'+str(row)] = str(time)
        ws1['B'+str(row)] = str(air_temp)
        ws1['C'+str(row)] = str(hectopascals)
        ws1['D'+str(row)] = str(humidity)
        ws1['E'+str(row)] = str(water_temp)
        ws1['F'+str(row)] = str(ph)
        row += 1
        
        print ('Timestamp = {0:0.3f}'.format(bme_sensor.t_fine))
        print ('Air_Temp  = {0:0.3f} deg C'.format(air_temp))
        print ('Pressure  = {0:0.2f} hPa'.format(hectopascals))
        print ('Humidity  = {0:0.2f} %'.format(humidity))
        print ("Water_Temp = " + str(water_temp) + " deg C")
        print ("pH = " + str(ph) + "pH")
        print("-------------------------------------------------")
        time.sleep(1)
        
except KeyboardInterrupt:
    print(" Finished")
workbook.close()
