from user_CRUD import database_user as userDB
import re

def login(email, pwd):
    # Return true is the user doesn't exist, return user infomation if the user exist
    return userDB.getUser(email, pwd)

def register(username, email, pwd):
    # Check if email exist, then check email formmat. If both pass, create the user
    if userDB.getUser(email):
        print("A account with this email already exist")
    elif not checkEmailFormat(email):
        print("The email formmat is wrong.")
    else:
        userDB.create(username, email, pwd)
        print("Inserted user: " + username + " " + email + " " + pwd)
        return True
    return False

def checkEmailFormat(email: str):
    # Check if anything before @ is from a-z and 0-9 and if anything after @ is a-z and must have atleast 2 characters
    return re.search("^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$", email)