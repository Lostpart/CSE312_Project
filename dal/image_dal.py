from bson import ObjectId


def insert(user_id: ObjectId, filename: str, image_collection):
    data = {"user_id": user_id, "filename": filename}
    return image_collection.insert_one(data)


def get_by_str_id(image_id: str, image_collection):
    return image_collection.find_one({"_id": ObjectId(image_id)})


def get_image_by_image_id(image_id: ObjectId, image_collection):
    return image_collection.find_one({"_id": image_id})


def get_image_filename_by_image_id(image_id: ObjectId, image_collection):
    return image_collection.find_one({"_id": image_id})["filename"]
