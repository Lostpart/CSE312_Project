import json
import sys

from flask import Flask, request
from flask_socketio import SocketIO

from dal import connect_database, chat_db
from chat import chat_controller
from dal.connect_database import connect_databases
from manager import user_manager
from controller import user_controller

app = Flask(__name__, static_url_path='')
# Python Socket code from 2019 Spring CSE 116
socket_server = SocketIO(app, cors_allowed_origins='*')


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/chatHistory")
def chat_history():
    data = json.loads(request.get_data(as_text=True))
    receive = chat_db.chat_history(data, chat_collection)
    return receive


# -------------- socket_server ------------------

@app.route("/login", methods=["POST"])
def home_login():
    return user_manager.login(request.json['email'], request.json['password'], user_collection)


@app.route("/register", methods=["POST"])
def home_register():
    return user_manager.register(request.json['displayName'], request.json['email'], request.json['password'],
                                 user_collection)

@app.route("/settings", methods = ["POST"])
def update_settings():
    return user_controller.set_user_setting(user_collection, request.json['user_id'], request.json['color'])


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


@socket_server.on('send_chat')
def send_chat(rawdata):
    check, answer = chat_controller.controller(rawdata)
    if check:
        socket_server.emit('error', json.dumps(answer))
    else:
        socket_server.emit('new_chat', json.dumps(answer["response"]), room=json.dumps(answer["to"]))
    pass


@socket_server.on('test_moment')
def send_moment(rawdata):
    # call moment function
    socket_server.emit('test_moment', rawdata, broadcast=True)


# ------------------ test_route -------------------
@app.route("/test-sendchat", methods=["POST"])
def test_send_chat():
    data = json.loads(request.get_data(as_text=True))
    print(data)
    mock_chat_collection = connect_database.connect_databases(["test-chat"])  # connect db
    mock_chat_collection = mock_chat_collection["test-chat"]
    receive = chat_db.send_chat(data, mock_chat_collection)
    return "success"


@app.route("/test-getchat")
def test_chat_history():
    data = json.loads(request.get_data(as_text=True))
    mock_chat_collection = connect_database.connect_databases(["test-chat"])  # connect db
    mock_chat_collection = mock_chat_collection["test-chat"]
    receive = chat_db.chat_history(data, mock_chat_collection)
    mock_chat_collection.delete_many({})
    return receive


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
