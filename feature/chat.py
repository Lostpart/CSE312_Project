
from bson import ObjectId
from dal import connect_database


def sendChat(data): #add chat
    chatCollection = connect_database.connect_databases(["chat"])
    from_user = data["from"]
    to_user = data["to"]
    message = data["message"]
    image = data["image"]
    if(image!=None):
        # call image function
        pass
    chatCollection.insert_one({"from":ObjectId(from_user),"to":ObjectId(to_user),"message":message, "image":image})
    return

def chatHistory(data): #chat history
    # return list
    list1 = []
    user_from = data["from"]
    user = data["to"]
    # get collection
    chatCollection = connect_database.connect_databases(["chat"])
    getchatCollection = connect_database.connect_databases(["chattmp"])

    # get chat 1
    answer1=chatCollection.find({"from":ObjectId(user_from),"to":ObjectId(user)})
    for data in answer1:
        getchatCollection.insert_one(data)

    # get chat 2 (reverse from and to)
    answer2=chatCollection.find({"from": ObjectId(user), "to": ObjectId(user_from)})
    for data in answer2:
        getchatCollection.insert_one(data)

    # get all chat sort by timestamp in _id
    final_answer=chatCollection.find({}).sort([['_id', -1]])
    for data in final_answer :
        list1.append(data)

    # clean collection
    getchatCollection.remove({})
    return list1
