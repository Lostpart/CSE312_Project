import json

from flask_socketio import join_room

from dal import connect_database, chat_db


def controller(rawdata):
    # rawdata {"from": str, "to": str, "message": str, "image": null}
    check, note = check_data(rawdata)  # check chat format
    if not check:  # error message
        error_msg = {"status": "error", "message": note}
        return False, error_msg
    else:
        data = json.loads(rawdata)
        chat_collection = connect_database.connect_databases(["chat"])  # connect db
        chat_collection = chat_collection["chat"]
        chat_db.send_chat(data, chat_collection, note)  # store chat into db
        to = data["to"]
        join_room(to)
        print("Client→Python：{}".format(data))
        response = {"status": True, "message": data}  # send new chat
        # close db connection
        return True, {"to": to, "response": response}


def check_data(rawdata):  # revise check json, check "from", "to", "message", "image" exists
    image_check = True
    try:
        data = json.loads(rawdata)
    except:
        return False, "rawdata is not json format"
    try:
        from_user = data["from"]
    except:
        return False, "'from' is not exists"
    try:
        to = data["to"]
    except:
        return False, "'to' is not exists"
    try:
        chat = data["message"]
    except:
        return False, "'message' is not exists"
    try:
        image = data["image"]
    except:
        image_check = False

    if not isinstance(from_user, str):
        return False, "from is not string"
    if not isinstance(to, str):
        return False, "to is not string"
    if not isinstance(chat, str):
        return False, "chat is not string"
    if image_check:
        if not isinstance(image, str):
            return False, "image is not string"
    if len(from_user) != 24:
        return False, "from is not consistent with ObjectId format"
    if len(to) != 24:
        return False, "to is not consistent with ObjectId format"
    return True, image_check