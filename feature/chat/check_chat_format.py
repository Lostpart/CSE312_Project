def check_data(data):
    from_user = data["from"]
    to = data["to"]
    chat = data["message"]
    image = data["image"]
    if (not isinstance(from_user, str)):
        return False, "from is not string"
    if (not isinstance(to, str)):
        return False, "to is not string"
    if (not isinstance(chat, str)):
        return False, "chat is not string"
    if (not isinstance(image, str)):
        return False, "image is not string"
    if (len(from_user) != 24):
        return False, "from is not consistent with ObjectId format"
    if (len(to) != 24):
        return False, "to is not consistent with ObjectId format"
    return True, "correct format"
