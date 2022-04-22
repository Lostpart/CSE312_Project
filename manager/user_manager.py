import re
from dal import user_dal as userDB
import json


def login(email, password):
    # Return true is the user doesn't exist, return user infomation if the user exist
    message = userDB.get_user(None, email, password)
    if not message["status"]:
        message["status"] = "Error"
        return json.dumps(message)
    elif message["status"]:
        return json.dumps(message["message"])

def register(displayName, email, password):
    # Check if email exist, then check email formmat. If both pass, create the user
    status_message = userDB.get_user(None, email)
    status = status_message["status"]
    if  status:
        # print("A account with this email already exist")
        error_message = "A account with this email already exist."
        return json.dumps(userDB.construct_return_message("Error", error_message))
    elif not check_email_format(email):
        # print("The email formmat is wrong.")
        error_message = "The email formmat is wrong."
        return json.dumps(userDB.construct_return_message("Error", error_message))
    elif password == "":
        error_message = "password can't be empty"
        return json.dumps(userDB.construct_return_message("Error", error_message))
    else:
        userInfor = userDB.create(displayName, email, password)
        # print("Inserted user: " + username + " " + email + " " + password)
        return json.dumps(userInfor)
    # return False

def check_email_format(email: str):
    # Check if anything before @ is from a-z and 0-9 and if anything after @ is a-z and must have atleast 2 characters
    return re.search("^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$", email)