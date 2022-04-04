"""This module is to handle CRUD for user"""
from pymongo import MongoClient
import datetime as dt

"""This object contain the CRUD functions for user"""
def create(user: str, email:str, password: str):
    """Create user info and store it in DB["user"]"""
    users_collection = connect_user_DB()
    current_time = getCurrentTime()
    user_dict = {"username": user, "email": email, "password": password, "last_update_time": current_time}
    users_collection.insert_one(user_dict)

def getUser(id = None, email: str = None, password: str = None):
    # 用户登录时我们并不知道id，所以必须用email来查询
    users_collection = connect_user_DB()
    user_dict = None
    if email != None:
        user_dict = users_collection.find_one({"email": email})
    elif id != None:
        user_dict = users_collection.find_one({"email": id})
    else:
        print("Please enter account information")
        return False
    if user_dict:
        print("Find user")
        if password == None:
            return user_dict
        elif user_dict["password"] == password:
            return user_dict
        else:
            print("Your email or password is wrong")
            return False        
    else:
        return False

def updateUser(id: object, email: str = None, username: str = None, password: str = None):
    # updateUser("A", email, "B") will update field A with data B for account "email"
    # Example: updateUser("username", "123@gmail.com", "howie") will update 123@gmail.com's username to howie
    # This function doesn't check email formmat, make check the email formatt before calling this
    users_collection = connect_user_DB()
    user_dict = users_collection.find_one({"_id": id})
    if user_dict:
        updated_user_dict = dict()
        current_time = getCurrentTime()
        temp_dict = dict({"email": email, "username": username, "password": password, "last_update_time": current_time})
        for key in temp_dict:
            if temp_dict[key] != None:
                updated_user_dict[key] = temp_dict[key]
        print(updated_user_dict)
        users_collection.update_one({"_id": id}, {"$set": updated_user_dict})
        return True
    else:
        print("User account not found")
        return False

def deleteUser(id: object):
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