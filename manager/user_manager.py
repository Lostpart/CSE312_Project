import re
from dal import user_dal
import json


def login(email, password, user_collection):
    # Return true is the user doesn't exist, return user infomation if the user exist
    message = user_dal.get_user(user_collection=user_collection, email=email, password=password)
    if not message["status"]:
        message["status"] = "Error"
        return json.dumps(message)
    elif message["status"]:
        return json.dumps(message["message"])
    else:
        return json.dumps(message)


def register(username, email, password, user_collection):
    # Check if email exist, then check email formmat. If both pass, create the user
    status_message = user_dal.get_user(user_collection, email=email)
    status = status_message["status"]
    if status:
        # print("A account with this email already exist")
        error_message = "A account with this email already exist."
        return json.dumps(user_dal.construct_return_message("Error", error_message))
    elif not check_email_format(email):
        # print("The email formmat is wrong.")
        error_message = "The email formmat is wrong."
        return json.dumps(user_dal.construct_return_message("Error", error_message))
    elif password == "":
        error_message = "password can't be empty"
        return json.dumps(user_dal.construct_return_message("Error", error_message))
    else:
        userInfor = user_dal.create(user_collection, username, email, password)
        # print("Inserted user: " + username + " " + email + " " + password)
        return json.dumps(userInfor)
    # return False


def get_all_user(users_collection):
    """ Return user list in json format like this
        {{"displayName": displayName, "email": email, "user_id": id, "active": True/False}, .......}
    """
    return json.dumps(user_dal.retrieve_all(users_collection))


def get_active_user(users_collection):
    return json.dumps(user_dal.retrieve_active_user(users_collection))


def set_active(user_collection, user_id, status):
    return json.dumps(user_dal.update_user(user_collection, user_id, "active", status))


def check_email_format(email: str):
    # Check if anything before @ is from a-z and 0-9 and if anything after @ is a-z and must have atleast 2 characters
    return re.search("^([a-z0-9_.-]+)@([\da-z.-]+)\.([a-z.]{2,6})$", email)


def get_user_by_id(user_collection, id):
    result = user_dal.get_user(user_collection, id=id)
    if result["status"] == False:
        result["status"] = "Error"
    else:
        result = result["message"]
    return json.dumps(result)
    # return  user_dal.get_user_by_id(user_collection, id)


def get_user_by_email(user_collection, email):
    result = user_dal.get_user(user_collection, email=email)
    if result["status"] == False:
        result["status"] == "Error"
    else:
        result = result["message"]
    return json.dumps(result)


def delete_user(user_collection, id):
    0


def set_settings(user_collection, user_id, settings):
    user_dal.update_user(user_collection, user_id, "settings", settings)
    return user_dal.get_user(user_collection, user_id)
