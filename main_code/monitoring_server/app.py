from flask import Flask, render_template
from openpyxl import Workbook
from openpyxl.compat import range
from w1thermsensor import W1ThermSensor
from datetime import datetime
#from Adafruit_BME280 import * doesnt work -_-
import time

app = Flask(__name__)

my_data = ['Water pH','Water Temperature','External Temperature','External Humidity']


@app.route('/')
def index(sensor=None):
    return render_template('index.html',my_data=my_data)


if __name__ == "__main__":
    app.run(debug=True)
