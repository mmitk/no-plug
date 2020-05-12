from flask import Flask
from flask_socketio import SocketIO, join_room, emit, send
import user


# initialize Flask
app = Flask(__name__)
socketio = SocketIO(app)
ROOMS = {} # dict to track active rooms

#@app.route('/script-endpoint')
#def index():


@socketio.on('create')
def on_create(data):
    us = user.User()
    room = us.user_id
    ROOMS[room] = us
    join_room(room)
    emit('join_room',{'room':room})


if __name__ == '__main__':
    socketio.run(app, debug=True)