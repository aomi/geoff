import xlsxwriter
from w1thermsensor import W1ThermSensor
from datetime import datetime
from Adafruit_BME280 import *
import time

name = raw_input("Name of Document? ")

workbook = xlsxwriter.Workbook(str(name)+'.xlsx')
worksheet = workbook.add_worksheet("Temperature Data")
bold = workbook.add_format({"bold":True})

bme_sensor = BME280(mode=BME280_OSAMPLE_8)
water_temp_sensor = W1ThermSensor()

worksheet.write("A1", "Time", bold)
worksheet.write(0, 1, "Air_Temp Values (C)")
worksheet.write(0, 1, "Pressure Values (hPa)")
worksheet.write(0, 1, "Humidity Values (%)")
worksheet.write(0, 1, "Water_Temp Values (C)")
row = 1

try:
    while True:
        
        air_temp     = bme_sensor.read_temperature()
        pascals      = bme_sensor.read_pressure()
        hectopascals = pascals / 100
        humidity     = bme_sensor.read_humidity()
        water_temp   = water_temp_sensor.get_temperature()
        time = datetime.now()
        
        worksheet.write(row, 0, time)
        worksheet.write(row, 1, air_temp)
        worksheet.write(row, 2, hectopascals)
        worksheet.write(row, 3, humidity)
        worksheet.write(row, 4, water_temp)
        row += 1
        
        print ('Timestamp = {0:0.3f}'.format(bme_sensor.t_fine))
        print ('Air_Temp  = {0:0.3f} deg C'.format(air_temp))
        print ('Pressure  = {0:0.2f} hPa'.format(hectopascals))
        print ('Humidity  = {0:0.2f} %'.format(humidity))
        print ("Water_Temp = " + str(water_temp) + " deg C")
        print("-------------------------------------------------")
        time.sleep(1)
        
except KeyboardInterrupt:
    print(" Finished")
workbook.close()
