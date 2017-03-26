from peewee import *
db = SqliteDatabase('database.db')

# configuration of database models for sensor data storage


class Sensor(Model):
    sensor_type = CharField()
    data = FloatField()
    date = DateField()
    unit = CharField()
    key = PrimaryKeyField()

    class Meta:
        database = db


