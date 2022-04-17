import json

from bson import ObjectId
from dal import connect_database
from manager import image_manager

def send_chat(data): #add chat
    chat_collection = connect_database.connect_databases(["chat"])
    chat_collection = chat_collection["chat"]
    from_user = data["from"]
    to_user = data["to"]
    message = data["message"]
    image_data = data["image"]
    image_id = None
    if(image_data != None):
        image_id = image_manager.add_image_by_base64(image_data)
    chat_collection.insert_one({"from": ObjectId(from_user), "to": ObjectId(to_user), "message": message, "image": image_id})
    return

def chat_history(data): #chat history
    # return list
    list1 = []
    user_from = data["from"]
    user = data["to"]
    # get collection
    chat_collection = connect_database.connect_databases(["chat"])
    chat_collection = chat_collection["chat"]
    chat_tmp_collection = connect_database.connect_databases(["chat_tmp"])
    chat_tmp_collection = chat_tmp_collection["chat_tmp"]

    # clean temp collection
    chat_tmp_collection.delete_many({})

    # get chat 1
    answer1 = chat_collection.find({"$and": [{"from": {"$eq": ObjectId(user_from)}}, {"to": {"$eq": ObjectId(user)}}]})
    for data in answer1:
        chat_tmp_collection.insert_one(data)

    # get chat 2 (reverse from and to)
    answer2 = chat_collection.find({"$and": [{"from": {"$eq": ObjectId(user)}}, {"to": {"$eq": ObjectId(user_from)}}]})
    for data in answer2:
        chat_tmp_collection.insert_one(data)

    # get all chat sort by timestamp in _id
    final_answer = chat_collection.find({}).sort([['_id', 1]])
    for i in final_answer:
        del i["_id"]
        i["from"] = str(i["from"])
        i["to"] = str(i["to"])
        list1.append(i)


    # clean collection
    chat_tmp_collection.delete_many({})
    return json.dumps(list1)
