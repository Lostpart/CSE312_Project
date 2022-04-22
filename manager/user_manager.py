import re
from dal import user_dal
import json


def login(email, password, users_collection):
    # Return true is the user doesn't exist, return user infomation if the user exist
    message = user_dal.get_user(users_collection, email=email, password=password)
    if message["status"]:
        return json.dumps(message["message"])
    else:
        return json.dumps(message)


def register(username, email, password, users_collection):
    # Check if email exist, then check email formmat. If both pass, create the user
    status_message = user_dal.get_user(users_collection, email=email)
    status = status_message["status"]
    if status:
        # print("A account with this email already exist")
        error_message = "A account with this email already exist."
        return user_dal.construct_return_message("Error", error_message)
    elif not checkEmailFormat(email):
        # print("The email formmat is wrong.")
        error_message = "The email formmat is wrong."
        return user_dal.construct_return_message("Error", error_message)
    elif password == "":
        error_message = "password can't be empty"
        return user_dal.construct_return_message("Error", error_message)
    else:
        userInfor = user_dal.create(username, email, password)
        # print("Inserted user: " + username + " " + email + " " + password)
        return json.dumps(userInfor)
    # return False


def checkEmailFormat(email: str):
    # Check if anything before @ is from a-z and 0-9 and if anything after @ is a-z and must have atleast 2 characters
    return re.search("^([a-z0-9_.-]+)@([\da-z.-]+)\.([a-z.]{2,6})$", email)


def get_user_by_id(id, user_collection):
    # return user_dal.get_user(user_collection, id=id)
    return  user_dal.get_user_by_id(id, user_collection)
