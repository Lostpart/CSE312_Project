import json

from bson import ObjectId
from dal import connect_database
from manager import image_manager


def send_chat(data, chat_collection, image_check):  # add chat
    print(data, chat_collection, image_check)
    from_user = data["from"]
    to_user = data["to"]
    message = data["message"]
    image_id = None
    if image_check:
        print("here")
        image_data = data["image"]
        # image_id = image_manager.add_image_by_base64(from_user, image_data)
    chat_collection.insert_one(
        {"from": ObjectId(from_user), "to": ObjectId(to_user), "message": message, "image": image_id})
    print("finish")
    return


def chat_history(data, chat_collection):  # chat history
    # return list
    list1 = []

    user_from = data["from"]
    user = data["to"]

    # get collection
    chat_tmp_collection = connect_database.connect_databases(["chat_tmp"])
    chat_tmp_collection = chat_tmp_collection["chat_tmp"]

    # clean temp collection
    chat_tmp_collection.delete_many({})

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

    # clean collection
    chat_tmp_collection.delete_many({})
    # close chat_tmp_collection connection
    return json.dumps(list1)
