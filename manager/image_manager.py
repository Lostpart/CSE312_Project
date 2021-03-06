import base64
import hashlib
import os
import random
from bson import ObjectId

from dal import image_dal


def add_image_by_base64(user_id: ObjectId, image_data_base64: str, image_type: str, image_collection):
    return add_image(user_id, base64.b64decode(image_data_base64), image_type, image_collection)


def add_image(user_id: ObjectId, image_data: bytes, image_type: str, image_collection):
    random_bits = random.getrandbits(128).to_bytes(16, 'big')
    md5_filename = hashlib.md5(image_data+random_bits).hexdigest()
    image_filename = "{}.{}".format(md5_filename, image_type)
    
    if not os.path.exists("static/"):
        os.makedirs("static/")

    if not os.path.exists("static/upload-image/"):
        os.makedirs("static/upload-image/")
        
    with open("static/upload-image/{}".format(image_filename), "wb") as f:
        f.write(image_data)
    return image_dal.insert(ObjectId(user_id), image_filename, image_collection).inserted_id


def get_image_filename(image_id: ObjectId, image_collection):
    return image_dal.get_image_by_image_id(image_id, image_collection)["filename"]
