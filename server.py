import json
import sys

from flask import Flask
from flask_socketio import SocketIO
from flask import request

from dal.connect_database import connect_databases
from manager import user_manager

app = Flask(__name__, static_url_path='')
# Python Socket code from 2019 Spring CSE 116
socket_server = SocketIO(app, cors_allowed_origins='*')


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/login", methods=["POST"])
def home_login():
    return user_manager.login(request.json['email'], request.json['password'], user_collection)


@app.route("/register", methods=["POST"])
def home_register():
    return user_manager.register(request.json['displayName'], request.json['email'], request.json['password'],
                                 user_collection)


@socket_server.on('connect')
def test_connect():
    print('Client connected')
    socket_server.emit('connect', {'data': 'Connected'})


@socket_server.on('disconnect')
def test_disconnect():
    print('Client disconnected')


@socket_server.on('test_msg')
def test_msg(rawdata):
    # rawdata = str(request.data)
    print("Client→Python：{}".format(rawdata))
    response = json.dumps({"msg_type": "test_msg", "msg": rawdata})
    socket_server.emit('test_msg', response)
    pass


if __name__ == '__main__':
    port = 8080
    if len(sys.argv) >= 2:
        port = sys.argv[1]

    collection_list = ["user", "chat", "image", "moment"]
    db_list = connect_databases(collection_list)
    user_collection = db_list["user"]
    chat_collection = db_list["chat"]
    image_collection = db_list["image"]
    moment_collection = db_list["moment"]

    socket_server.run(app, host="0.0.0.0", port=port, debug=True)
