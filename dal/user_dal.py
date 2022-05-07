"""This module is used to handle CRUD for user"""
from unittest import result
from pymongo import MongoClient
import datetime as dt
import json

"""This object contain the CRUD functions for user"""


def create(user_collection, displayName: str, email: str, password: str):
    """Create user info and store it in DB["user"]"""
    current_time = get_current_time()
    user_dict = {"displayName": displayName, "email": email, "password": password, 
                    "last_update_time": current_time, "active": False, "settings": "blue"}
    user_collection.insert_one(user_dict)
    result_dic = {}
    fields = ["displayName", "email"]
    result_dic = construct_return_dict(user_dict, fields)
    result_dic["user_id"] = str(user_dict["_id"])
    return result_dic


def get_user(user_collection, id=None, email: str = None, password: str = None):
    # 用户登录时我们并不知道id，所以必须用email来查询
    # id和email至少要有一个
    user_dict = None
    if id is not None:
        user_dict = user_collection.find_one({"_id": id}, {"last_update_time": 0, "password": 0})
    elif email is not None and password is not None:
        user_dict = user_collection.find_one({"email": email, "password": password},
                                             {"last_update_time": 0, "password": 0})
    elif email is not None:
        user_dict = user_collection.find_one({"email": email}, {"last_update_time": 0, "password": 0})
    else:
        error_message = "information missing"
        return construct_return_message(False, error_message)
    if user_dict:
        result_dic = {}
        fields = ["displayName", "email", "settings"]
        result_dic = construct_return_dict(user_dict, fields)
        result_dic["user_id"] = str(user_dict["_id"])
        return construct_return_message(True, result_dic)
        # else:
        #     error_message = "Your email or password is wrong"
        #     return construct_return_message(False, "error_message", error_message)
    else:
        error_message = "User not found"
        return construct_return_message(False, error_message)

def get_user_by_id(id, user_collection):
    # 哥们，DAL写的太复杂了
    # return user_collection.find_one({"_id": id})
    return get_user(user_collection, id)

def get_user_by_email(user_collection, email):
    return get_user(user_collection, email=email)


def update_user(user_collection, id: object, key: str, value):
    # Not modified yet
    # update_user(user_collection, "A", "email", B) will update user A's email with data B
    # Example: update_user(user_collection, A, "email", "howie@asda.com") will update A's email to howie@asda.com
    # This function doesn't check email formmat, make check the email formatt before calling this
    user_dict = user_collection.find_one({"_id": id})
    if user_dict:
        user_collection.update_one({"_id": id}, {"$set": {key: value}})
        user_dict = user_collection.find_one({"_id": id})
        fields = ["displayName", "email", "active"]
        # print(updated_user_dict)
        result_dic = construct_return_dict(user_dict, fields)
        result_dic["user_id"] = str(user_dict["_id"])
        return result_dic
    else:
        error_message = "User account not found"
        return_message_json = {"status": "Error", "message": error_message}
        return return_message_json


def delete_user(id: object):
    return 0

def retrieve_all(user_collection):
    all_users_with_object_id = list(user_collection.find({}, {"displayName": 1, "active": 1, "_id": 1, "email": 1}))
    all_users = []
    for user in all_users_with_object_id:
        temp_user = user
        id =  str(user["_id"])
        temp_user["user_id"] = id
        temp_user.pop("_id")
        all_users.append(temp_user)
    return all_users
def retrieve_active_user(user_collection):
    all_users_with_object_id = list(user_collection.find({"active": True}, {"displayName": 1, "active": 1, "_id": 1, "email": 1}))
    all_users = []
    for user in all_users_with_object_id:
        temp_user = user
        id =  str(user["_id"])
        temp_user["user_id"] = id
        temp_user.pop("_id")
        all_users.append(temp_user)
    return all_users
    
# def connect_user_DB():
#     # I'm using localhost. If you're using remote server, please change MongoClient in your need
#     # Data formmater: CSE312 -> user
#     #                         -> image, etc
#     mongo_client = MongoClient("mongodb://localhost:27017")
#     db = mongo_client["CSE312"]
#     users_collection = db["user"]
#     return users_collection

# def drop_table(database, table: str):
#     if table in database.list_collection_names():
#         expect_table = database[table]
#         expect_table.drop()
#         # message = "Table " + table + "dropped"
#         return True
#     else:
#         error_message = "Table " + table + " doesn't exist"
#         return error_message


def construct_return_message(status, message):
    return_message_dict = {"status": status, "message": message}
    return return_message_dict


def construct_return_dict(user_dict, fields):
    return_dict = {}
    for field in fields:
        return_dict[field] = user_dict[field]
    return return_dict


def get_current_time():
    # Get current time as time Object. 
    # Use return.date to get date, return.hour to get hour, etc
    return dt.datetime.now()
