"""This module is used to handle CRUD for user"""
from unittest import result
from pymongo import MongoClient
import datetime as dt
import json

"""This object contain the CRUD functions for user"""
def create(displayName: str, email:str, password: str):
    """Create user info and store it in DB["user"]"""
    # Return {"displayername": displayname, "email": email, "user_id": id}
    users_collection = connect_user_DB()
    current_time = get_current_time()
    user_dict = {"displayName": displayName, "email": email, "password": password, "last_update_time": current_time}
    users_collection.insert_one(user_dict)
    result_dic = {}
    result_dic["user_id"] = str(user_dict["_id"])
    result_dic["displayName"] = user_dict["displayName"]
    result_dic["email"] = user_dict["email"]
    return result_dic


def get_user(id = None, email: str = None, password: str = None):
    # 用户登录时我们并不知道id，所以必须用email来查询
    users_collection = connect_user_DB()
    user_dict = None
    # print(id, email, password)
    if id is not None:
        user_dict = users_collection.find_one({"_id": id}, {"last_update_time": 0})
        # print(user_dict)
    elif email is not None and password is not None:
        user_dict = users_collection.find_one({"email": email, "password": password}, {"last_update_time": 0})
        # print(user_dict)
    elif email is not None:
        user_dict = users_collection.find_one({"email": email}, {"last_update_time": 0})
    else:
        error_message = "information missing"
        return construct_return_message(False, error_message)
    if user_dict:
        user_dict["user_id"] = str(user_dict["_id"])
        user_dict.pop("_id")
        user_dict.pop("password")
        userInfo = user_dict
        return construct_return_message(True, userInfo)
        # else:
        #     error_message = "Your email or password is wrong"
        #     return construct_return_message(False, "error_message", error_message)
    else:
        error_message = "User not found"
        return construct_return_message(False, error_message)

def update_user(id: object, email: str = None, displayName: str = None, password: str = None):
    # Not modified yet
    # update_user("A", email, "B") will update field A with data B for account "email"
    # Example: update_user("displayName", "123@gmail.com", "howie") will update 123@gmail.com's displayName to howie
    # This function doesn't check email formmat, make check the email formatt before calling this
    users_collection = connect_user_DB()
    user_dict = users_collection.find_one({"_id": id})
    if user_dict:
        updated_user_dict = dict()
        current_time = get_current_time()
        temp_dict = dict({"email": email, "displayName": displayName, "password": password, "last_update_time": current_time})
        for key in temp_dict:
            if temp_dict[key] is not None:
                updated_user_dict[key] = temp_dict[key]
        # print(updated_user_dict)
        users_collection.update_one({"_id": id}, {"$set": updated_user_dict})
        return True
    else:
        error_message = "User account not found"
        return_message_json = {"status": "error", "error_message": error_message}
        return return_message_json

def delete_user(id: object):
    return 0
    
def connect_user_DB():
    # I'm using localhost. If you're using remote server, please change MongoClient in your need
    # Data formmater: appName -> user
    #                         -> image, etc
    mongo_client = MongoClient("mongodb://localhost:27017")
    db = mongo_client["CSE312"]
    users_collection = db["user"]
    return users_collection

def construct_return_message(status, message):
    return_message_dict = {"status": status, "message": message}
    return return_message_dict

def get_current_time():
    # Get current time as time Object. 
    # Use return.date to get date, return.hour to get hour, etc
    return dt.datetime.now()