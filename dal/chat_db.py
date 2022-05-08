import json

import mongomock
from bson import ObjectId
from dal import connect_database
from manager import image_manager


def send_chat(data, chat_collection, image_check):  # add chat
    from_user = data["from"]
    to_user = data["to"]
    message = data["message"]
    image_id = None
    if image_check:
        image_data = data["image"]
        # image_id = image_manager.add_image_by_base64(from_user, image_data)
    chat_collection.insert_one(
        {"from": ObjectId(from_user), "to": ObjectId(to_user), "message": message, "image": image_id})
    return

def get_data(data, chat_collection):
    from_user = data["from"]
    to_user = data["to"]
    list = []
    data1 = chat_collection.find(
        {"from": ObjectId(from_user), "to": ObjectId(to_user)})
    if data1 is not None:
        for i in data1:
            i["_id"] = str(i['_id'])
            i["from"] = str(i["from"])
            i["to"] = str(i["to"])
            list.append(i)
    data2 = chat_collection.find(
        {"from": ObjectId(to_user), "to": ObjectId(from_user)})
    if data2 is not None:
        for i in data2:
            i["_id"] = str(i['_id'])
            i["from"] = str(i["from"])
            i["to"] = str(i["to"])
            list.append(i)
    return sorted(list, key = lambda i: i['_id'])

'''
def chat_history(data, chat_collection):  # chat history
    # return list
    list1 = []

    user_from = data["from"]
    user = data["to"]

    # get collection
    chat_tmp_collection = mongomock.MongoClient()["test-chat_db"]
    chat_tmp_collection = chat_tmp_collection["test-chat_db"]

    # get chat 1
    answer1 = chat_collection.find({"from": ObjectId(user_from), "to": ObjectId(user)})
    for data in answer1:
        chat_tmp_collection.insert_one(data)

    # get chat 2 (reverse from and to)
    answer2 = chat_collection.find({"from": ObjectId(user), "to": ObjectId(user_from)})
    for data in answer2:
        chat_tmp_collection.insert_one(data)

    # get all chat sort by timestamp in _id
    final_answer = chat_tmp_collection.find({}).sort([['_id', 1]]).limit(100)
    for i in final_answer:  # change to return format
        del i["_id"]
        i["from"] = str(i["from"])
        i["to"] = str(i["to"])
        list1.append(i)

    # close chat_tmp_collection connection
    return json.dumps(list1)
'''