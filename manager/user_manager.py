import re
from user_CRUD import database_user as userDB
import json


def login(email, password):
    # Return true is the user doesn't exist, return user infomation if the user exist
    message = userDB.getUser(None, email, password)
    if message["status"] == False:
        return json.dumps(message)
    elif message["status"] == True:
        return json.dumps(message["message"])

def register(username, email, password):
    # Check if email exist, then check email formmat. If both pass, create the user
    status_message = userDB.getUser(None, email)
    status = status_message["status"]
    if  status == True:
        # print("A account with this email already exist")
        error_message = "A account with this email already exist."
        return userDB.constructReturnMessage("Error", error_message)
    elif not checkEmailFormat(email):
        # print("The email formmat is wrong.")
        error_message = "The email formmat is wrong."
        return userDB.constructReturnMessage("Error", error_message)
    elif password == "":
        error_message = "password can't be empty"
        return userDB.constructReturnMessage("Error", error_message)
    else:
        userInfor = userDB.create(username, email, password)
        # print("Inserted user: " + username + " " + email + " " + password)
        return json.dumps(userInfor)
    # return False

def checkEmailFormat(email: str):
    # Check if anything before @ is from a-z and 0-9 and if anything after @ is a-z and must have atleast 2 characters
    return re.search("^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$", email)