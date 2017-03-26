from flask import render_template, request
from app import app
import tasks
import redis


rdb = redis.StrictRedis(host='localhost', port=6379, db=0)

# type of sensors to display in view
sensors = {
    'air_temp': {
        'name': 'Air Temperature',
        'unit': 'Celsius',
        'value': 'Please Refresh'
    },
    'water_temp': {
        'name': 'Water Temperature',
        'unit': 'Celsius',
        'value': 'Please Refresh'
    },
    'ph': {
        'name': 'pH',
        'unit': 'pH',
        'value': 'Please Refresh'
    },
    'humidity': {
        'name': 'Humidity',
        'unit': '%',
        'value': 'Please Refresh'
    },
    'pressure': {
        'name': 'Pressure',
        'unit': 'Pascals',
        'value': 'Please Refresh'
    }
}


# display a homepage
@app.route('/')
def index():
    tasks.get_sensor_data('ph')
    return render_template('index.html', data=sensors)


# send the last value collected through a GET method
@app.route('/sensor/<sensor_select>', methods=['GET'])
def data_send(sensor_select):
    if request.method == 'GET':
        if sensor_select == 'all':
            tasks.get_sensor_data.delay('pressure')
            tasks.get_sensor_data.delay('humidity')
            tasks.get_sensor_data.delay('air_temp')
            tasks.get_probe_data.delay()
            return 'all'
        return rdb.get(sensor_select)
    else:
        return 'Invalid Sensor'
