from flask import Flask
from flask_socketio import SocketIO
from celery import Celery


app = Flask(__name__)
app.debug = True

# celery configuration
app.config['CELERY_BROKER_URL'] = 'amqp://guest:guest@localhost:5672//'
app.config['CELERY_IMPORTS'] = 'tasks'

# celery initialization
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


# start flask server with SocketIO
socketio = SocketIO(app)

