from bson import ObjectId


def insert(user_id: ObjectId, content: str, image_list, moment_collection):
    data = {"from": user_id, "content": content}
    if len(image_list) > 0:
        data["image_list"] = image_list
    return moment_collection.insert_one(data)


def get_recent_moments(moment_collection, limit=1000):
    return moment_collection.find().sort({"_id": -1}).limit(limit)


def like_moment(moment_id: ObjectId, moment_collection):
    return moment_collection.find_one_and_update({"_id": moment_id}, {"$inc": {"like": 1}})
