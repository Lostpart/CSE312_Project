import json
import sys

from flask import Flask, request
from flask_socketio import SocketIO, join_room

from dal import connect_database
from feature.chat import chat_db, check_chat_format, chat_controller

app = Flask(__name__, static_url_path='')
# Python Socket code from 2019 Spring CSE 116
socket_server = SocketIO(app, cors_allowed_origins='*')


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/sendchat", methods=["POST"])
def test_send_chat():
    data = json.loads(request.get_data(as_text=True))
    mock_chat_collection = connect_database.connect_databases(["chat"])  # connect db
    mock_chat_collection = mock_chat_collection["chat"]
    receive = chat_db.send_chat(data, mock_chat_collection)
    return "success"


@app.route("/chatHistory")
def chat_history():
    data = json.loads(request.get_data(as_text=True))
    chat_collection = connect_database.connect_databases(["chat"])  # connect db
    chat_collection = chat_collection["chat"]
    receive = chat_db.chat_history(data, chat_collection)
    return receive


# -------------- socket_server ------------------

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
def send_memory(rawdata):
    # call memory function
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
    socket_server.run(app, host="0.0.0.0", port=port, debug=True)
