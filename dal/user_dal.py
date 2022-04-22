"""This module is used to handle CRUD for user"""
from pymongo import MongoClient
import datetime as dt
import json

"""This object contain the CRUD functions for user"""


def create(user_collection, displayName: str, email: str, password: str):
    """Create user info and store it in DB["user"]"""
    user_dict = {"displayName": displayName, "email": email, "password": password}
    user_collection.insert_one(user_dict)
    user_dict["user_id"] = str(user_dict["_id"])
    user_dict.pop("_id")
    user_dict.pop("password")
    return user_dict


def get_user(user_collection, id=None, email: str = None, password: str = None):
    # 用户登录时我们并不知道id，所以必须用email来查询
    user_dict = None
    # print(id, email, password)
    if id is not None:
        user_dict = user_collection.find_one({"_id": id})
        # print(user_dict)
    elif email is not None and password is not None:
        user_dict = user_collection.find_one({"email": email, "password": password})
        # print(user_dict)
    elif email is not None:
        user_dict = user_collection.find_one({"email": email})
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

def get_user_by_id(id, user_collection):
    # 哥们，DAL写的太复杂了
    return user_collection.find_one({"_id": id})


def update_user(user_collection, id: object, email: str = None, display_name: str = None, password: str = None):
    # Not modified yet
    # update_user("A", email, "B") will update field A with data B for account "email"
    # Example: update_user("displayName", "123@gmail.com", "howie") will update 123@gmail.com's displayName to howie
    # This function doesn't check email formmat, make check the email formatt before calling this
    user_dict = user_collection.find_one({"_id": id})
    if user_dict:
        updated_user_dict = dict()
        temp_dict = dict(
            {"email": email, "displayName": display_name, "password": password})
        for key in temp_dict:
            if temp_dict[key] != None:
                updated_user_dict[key] = temp_dict[key]
        # print(updated_user_dict)
        user_collection.update_one({"_id": id}, {"$set": updated_user_dict})
        return True
    else:
        error_message = "User account not found"
        return_message_json = {"status": "error", "error_message": error_message}
        return return_message_json


def delete_user(id: object):
    return 0


def construct_return_message(status, message):
    return_message_dict = {"status": status, "message": message}
    return return_message_dict

