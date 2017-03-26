from app import socketio
import tasks
import redis

# mini db client for getting data between python instances
rdb = redis.StrictRedis(host='localhost', port=6379, db=0)


# receive key press from client web browser for keydown events
@socketio.on('key_command')
def key_command(json):
    if json['data'] == 37:
        tasks.move_motor.delay('steer_motor', -1, 'manual')
    elif json['data'] == 39:
        tasks.move_motor.delay('steer_motor', 1, 'manual')
    elif json['data'] == 87:
        tasks.move_motor.delay('winch_motor', -1, 'manual')
    elif json['data'] == 83:
        tasks.move_motor.delay('winch_motor', 1, 'manual')
    elif json['data'] == 38:
        tasks.troll.delay('forward')
    elif json['data'] == 40:
        tasks.troll.delay('backward')


# same as above but for keydown events
@socketio.on('keyup')
def key_up(json):
    if json['data'] == 37 or json['data'] == 39:
        rdb.set('steer_motor', False)
    if json['data'] == 87 or json['data'] == 83:
        rdb.set('winch_motor', False)
    elif json['data'] == 38 or json['data'] == 40:
        tasks.troll.delay('stop')



