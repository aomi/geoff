from celery.schedules import crontab
from datetime import timedelta
import tasks

BROKER_URL = 'amqp://guest@localhost//'

COLLECTION_INTERVAL = 30


# functions to be ran in celery based on the interval (in seconds) listed above.
CELERYBEAT_SCHEDULE = {
    'air_temp': {
        'task': 'sensor',
        'schedule': timedelta(seconds=COLLECTION_INTERVAL),
        'args': ['air_temp'],
    },
    'probe': {
        'task': 'probe',
        'schedule': timedelta(seconds=COLLECTION_INTERVAL),
    },
    'pressure': {
        'task': 'sensor',
        'schedule': timedelta(seconds=COLLECTION_INTERVAL),
        'args': ['pressure'],
    },
    'humidity': {
        'task': 'sensor',
        'schedule': timedelta(seconds=COLLECTION_INTERVAL),
        'args': ['humidity'],
    }
}


