import xlsxwriter
from w1thermsensor import W1ThermSensor
from datetime import datetime

workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet("Temperature Data")
bold = workbook.add_format({"bold":True})

sensor = W1ThermSensor()

worksheet.write("A1", "Time", bold)
worksheet.write("A2", "Temp Values", bold)
try:
    while True:
        temp = sensor.get_temperature()


worksheet.write('A1', 'Sup maaaaan')

workbook.close()
