import json
import sys

from flask import Flask, request
from flask_socketio import SocketIO, join_room, leave_room

from controller.moment import moment_create_controller, moment_get_recent_moment_controller, moment_like
from dal import chat_db
from controller import chat_controller
from dal.connect_database import connect_databases
from manager import user_manager
from controller import user_controller
from static import USER_ONLINE, USER_OFFLINE

app = Flask(__name__, static_url_path='')
# Python Socket code from 2019 Spring CSE 116
socket_server = SocketIO(app, cors_allowed_origins='*')
sid_to_user_id = {}


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/chatHistory", methods=["POST"])
def chat_history():
    data = json.loads(request.get_data(as_text=True))
    receive = chat_db.get_data(data, chat_collection)
    return json.dumps(receive)


# -------------- socket_server ------------------

@app.route("/login", methods=["POST"])
def home_login():
    return user_manager.login(request.json['email'], request.json['password'], user_collection)


@app.route("/register", methods=["POST"])
def home_register():
    return user_manager.register(request.json['displayName'], request.json['email'], request.json['password'],
                                 user_collection)

@app.route("/allusers", methods=["GET"])
def get_all_user():
    return user_manager.get_all_user(user_collection)


@app.route("/moment/create", methods=["POST"])
def moment_create():
    payload = request.data
    return moment_create_controller.create_controller(payload, image_collection, moment_collection)


@app.route("/moment/getRecentMoments", methods=["POST"])
def moment_get_recent_moments():
    payload = request.data
    return moment_get_recent_moment_controller.get_recent_moments_controller(payload, image_collection,
                                                                             moment_collection)
@app.route("/settings", methods = ["POST"])
def update_settings():
    return user_controller.set_user_setting(user_collection, request.json['user_id'], request.json['color'])


@socket_server.on('connect')
def connect(user_id):
    print('Client connected')
    global chess_map
    join_room(user_id)  # 创建自己的room
    socket_server.emit('connect', {'data': 'Connected'})
    socket_server.emit('update_map', str(json.dumps(chess_map)), broadcast=True)
    return


@socket_server.on('update_map')
def update_map(new_map):
    global chess_map
    chess_map = new_map
    socket_server.emit('update_map', str(json.dumps(chess_map)), broadcast=True)
    return


@socket_server.on('moment_like')
def ws_moment_like(payload):
    try:
        result = moment_like.moment_like_controller(payload, moment_collection)
    except ValueError as err:
        data = {"status": "error", "message": err}
        socket_server.send(json.dumps(data))
        return

    sending_json = json.dumps(result)
    socket_server.emit("moment_like", sending_json, broadcast=True)
    return


'''
@socket_server.on('test_msg')
def test_msg(rawdata):
    # rawdata = str(request.data)
    print("Client→Python：{}".format(rawdata))
    response = json.dumps({"msg_type": "test_msg", "msg": rawdata})
    socket_server.emit('test_msg', response)
'''


@socket_server.on('send_chat')
def send_chat(rawdata):
    check, answer = chat_controller.controller(rawdata, chat_collection)
    if check is False:
        socket_server.emit('error', json.dumps(answer))
    else:
        join_room(rawdata["to"])  # 发送前join_room, 发完直接leave_room
        socket_server.emit('new_chat', json.dumps(answer["response"]['message']), room=rawdata["to"])
        leave_room(rawdata["to"])
    return


@socket_server.on('join')
def on_join(data):
    user_id = data['room']
    user_controller.set_user_activity(user_id, USER_ONLINE, user_collection)

    room = data['room']
    join_room(room)
    socket_server.send(data['displayName'] + ' has entered the room.', room=room)
    return


@socket_server.on('leave')
def on_leave(data):
    user_id = data['room']
    user_controller.set_user_activity(user_id, USER_OFFLINE, user_collection)

    room = data['room']
    leave_room(room)
    socket_server.send(data['displayName'] + ' has left the room.', room=room)
    return


if __name__ == '__main__':
    port = 8080
    if len(sys.argv) >= 2:
        port = int(sys.argv[1])
    chess_map = {'map': [[None, None, None], [None, None, None], [None, None, None]], 'result': None, 'finished': False,
                 'n': 0}
    collection_list = ["user", "chat", "image", "moment"]
    db_list = connect_databases(collection_list)
    user_collection = db_list["user"]
    chat_collection = db_list["chat"]
    image_collection = db_list["image"]
    moment_collection = db_list["moment"]

    socket_server.run(app, host="0.0.0.0", port=port, debug=True)
