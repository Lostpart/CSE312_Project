from bson import ObjectId

from dal import moment_dal
from manager.image_manager import add_image_by_base64, get_image_filename
from utils import safe_html

accept_image_types = {"jpg", "png"}


def create_moment(user_id_str, content, images, image_collection, moment_collection):
    user_id = ObjectId(user_id_str)
    image_list = []

    for i in images:
        image_name = i['filename']
        image_data_base64 = i['file']
        image_type = image_name[image_name.rfind(".") + 1:]
        if image_type not in accept_image_types:
            print("Unsupported image type when processing {}".format(image_name))
            raise TypeError("Image type not supported")
        image_list.append(add_image_by_base64(user_id, image_data_base64, image_type, image_collection))

    content = safe_html(content)

    insert_result = moment_dal.insert(user_id, content, image_list, moment_collection)

    return {"moment_id": str(insert_result.inserted_id)}


def get_recent_moments(image_collection, moment_collection, limit=10):

    db_moment_list = moment_dal.get_recent_moments(moment_collection, limit=limit)
    moment_list = []

    for i in db_moment_list:
        moment_list.append({"moment_id": str(i["_id"]),
                            "from": str(i["from"]),
                            "time": int(i["_id"].generation_time.timestamp()),
                            "content": i["content"],
                            "image": [get_image_filename(j, image_collection) for j in (i.get("image", []))],
                            "like": int(i["like"])})

    return moment_list


def like_moment(moment_id, moment_collection):
    db_result = moment_dal.like_moment(ObjectId(moment_id), moment_collection)
    if db_result is None:
        raise LookupError("Can't find given moment")
    return db_result

