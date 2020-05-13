from flask import Flask, request, jsonify
from flask_socketio import SocketIO, join_room, emit, send
import user


# initialize Flask
app = Flask(__name__)
socketio = SocketIO(app)
ROOMS = {} # dict to track active rooms

@app.route('/script/status', methods = ['POST'])
def status_updated():
    return request.json['Status']

@app.route('/script/trigger', methods = ['POST'])
def trigger_broadcast():
    emit('data broadcast',{'Status':request.json['Status'],  'Precentage': request.json['Precentage']}, room = request.json['User'])

@socketio.on('connect', namespace='/begin')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('begin_recieving', namespace = '/begin')
def on_begin(user_id):
    us = user.User()
    room = user_id
    ROOMS[room] = us
    join_room(room)
    emit('join_room',{'room':room})




if __name__ == '__main__':
    socketio.run(app, debug=True)