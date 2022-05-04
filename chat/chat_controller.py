import json
from flask import escape
from dal import connect_database, chat_db


def controller(rawdata, collection):
    # rawdata {"from": str, "to": str, "message": str, "image": null}
    check, note = check_data(rawdata)  # check chat format
    if not check:  # error message
        error_msg = {"status": "error", "message": note}
        return False, error_msg
    else:
        data = rawdata
        chat_db.send_chat(data, collection, note)  # store chat into db
        to = data["to"]
        print("Client→Python：{}".format(data))
        msg = {}
        msg["from"] = data["from"]
        msg["to"] = data["to"]
        msg["message"] = data["message"]
        response = {"status": True, "message": data}  # send new chat
        # close db connection
        return True, {"to": to, "response": response}


def check_data(rawdata):  # revise check json, check "from", "to", "message", "image" exists
    image_check = True
    if type(rawdata) is not dict:
        try:
            data = json.loads(rawdata)
        except:
            return False, "rawdata is not json format"
    else:
        data = rawdata
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
