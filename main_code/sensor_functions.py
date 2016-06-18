from Adafruit_BME280 import *

bme_sensor = BME280(mode=BME280_OSAMPLE_8)

air_temp     = bme_sensor.read_temperature()
pascals      = bme_sensor.read_pressure()
hectopascals = pascals / 100
humidity     = bme_sensor.read_humidity()

print ('Timestamp = {0:0.3f}'.format(bme_sensor.t_fine))
print ('Air_Temp  = {0:0.3f} deg C'.format(air_temp))
print ('Pressure  = {0:0.2f} hPa'.format(hectopascals))
print ('Humidity  = {0:0.2f} %'.format(humidity))
