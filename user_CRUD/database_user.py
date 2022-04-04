"""This module is to handle CRUD for user"""
from pymongo import MongoClient
import datetime as dt

"""This object contain the CRUD functions for user"""
def create(user: str, email:str, pwd: str):
    """Create user info and store it in DB["user"]"""
    users_collection = connect_user_DB()
    current_time = str(getCurrentTime())
    user_dict = {"username": user, "email": email, "password": pwd, "last_update_time": current_time}
    users_collection.insert_one(user_dict)

def getUser(email: str, pwd: str = ""):
    users_collection = connect_user_DB()
    user_dict = users_collection.find_one({"email": email})
    if user_dict:
        print("Find user")
        if pwd == "":
            return True
        elif user_dict["password"] == pwd:
            return user_dict
        else:
            print("Your email or password is wrong")
            return False        
    else:
        return False

def updateUser(username: str, email: str, pwd: str):
    return 0

def deleteUser(email: str):
    return 0
def connect_user_DB():
    # I'm using localhost. If you're using remote server, please change MongoClient in your need
    # Data formmater: appName -> user
    #                         -> image, etc
    mongo_client = MongoClient("mongodb://localhost:27017")
    db = mongo_client["appName"]
    users_collection = db["user"]
    return users_collection

def getCurrentTime():
    # Get current time as time Object. 
    # Use return.date to get date, return.hour to get hour, etc
    return dt.datetime.now()