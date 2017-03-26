from app import socketio, app, tasks, views, triggers

# start flask server with socketio in debug mode on port listed below.
socketio.run(app,host='0.0.0.0', port=8080, debug=True)