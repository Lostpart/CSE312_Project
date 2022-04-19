from bson import ObjectId
from dal import connect_database


def send_chat(data): #add chat
    chat_collection = connect_database.connect_databases(["chat"])
    from_user = data["from"]
    to_user = data["to"]
    message = data["message"]
    image = data["image"]
    if(image!=None):
        # call image function
        pass
    chat_collection.insert_one({"from": ObjectId(from_user), "to": ObjectId(to_user), "message": message, "image": image})
    return

def chat_history(data): #chat history
    # return list
    list1 = []
    user_from = data["from"]
    user = data["to"]
    # get collection
    chat_collection = connect_database.connect_databases(["chat"])
    chat_tmp_collection = connect_database.connect_databases(["chattmp"])

    # get chat 1
    answer1 = chat_collection.find({"from": ObjectId(user_from), "to": ObjectId(user)})
    for data in answer1:
        chat_tmp_collection.insert_one(data)

    # get chat 2 (reverse from and to)
    answer2 = chat_collection.find({"from": ObjectId(user), "to": ObjectId(user_from)})
    for data in answer2:
        chat_tmp_collection.insert_one(data)

    # get all chat sort by timestamp in _id
    final_answer = chat_collection.find({}).sort([['_id', -1]])
    for data in final_answer:
        list1.append(data)

    # clean collection
    chat_tmp_collection.remove({})
    return list1
