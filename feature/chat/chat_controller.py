import json

from flask_socketio import join_room

from feature.chat import check_chat_format, chat_db


def controller(rawdata):
    # rawdata {"from": str, "to": str, "message": str, "image": null}
    data = json.loads(rawdata)
    check, note = check_chat_format.check_data(data)  # check chat format
    if check:  # error message
        error_msg = {"status": "error", "error_message": note}
        return False, error_msg
    else:
        chat_db.send_chat(data)  # store chat into db
        to = data["to"]
        join_room(to)
        print("Client→Python：{}".format(data))
        response = {"msg_type": "new_chat", "msg": data}  # send new chat
        return True, {"to": to, "response": response}
