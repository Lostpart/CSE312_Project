from dal import moment_dal
from manager.image_manager import add_image_by_base64
from manager.user_manager import get_user_by_id
from utils import safe_html

accept_image_types = {"jpg", "png"}


def create_moment(user_id_str, content, images, user_collection, image_collection, moment_collection):
    user_id = get_user_by_id(user_id_str, user_collection)["_id"]
    image_list = []

    for image_name, image_data_base64 in images.items():
        image_type = image_name[image_name.rfind(".") + 1:]
        if image_type not in accept_image_types:
            print("Unsupported image type when processing {}".format(image_name))
            continue
        image_list.append(add_image_by_base64(user_id, image_data_base64, image_type, image_collection))

    content = safe_html(content)

    insert_result = moment_dal.insert(user_id, content, image_list, moment_collection)

    return {"moment_id": insert_result.inserted_id}
