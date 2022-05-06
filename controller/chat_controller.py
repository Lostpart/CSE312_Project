import json
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
        response = {"status": True, "message": data}  # send new chat
        # close db connection
        return True, {"to": to, "response": response}


def check_data(rawdata):  # revise check json, check "from", "to", "message", "image" exists
    image_check = True
    if type(rawdata) is not dict:
        return False, "rawdata is not dict type"
    else:
        data = rawdata
    try:
        from_user = data["from"]
    except KeyError:
        return False, "'from' is not exists"
    try:
        to = data["to"]
    except KeyError:
        return False, "'to' is not exists"
    try:
        chat = data["message"]
    except KeyError:
        return False, "'message' is not exists"
    try:
        image = data["image"]
    except KeyError:
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


def html_escape(msg):
    msg = msg.replace("&", "&amp;")
    msg = msg.replace("<", "&lt;")
    msg = msg.replace(">", "&gt;")
    msg = msg.replace('"', "&quot;")
    msg = msg.replace("'", "&apos;")
    return msg
