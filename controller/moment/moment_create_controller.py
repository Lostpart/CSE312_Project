import json

from manager.moment_manager import create_moment


def create_controller(payload, image_collection, moment_collection):
    if payload is None:
        return on_fail("Invalid input: No payload")
    try:
        data = json.loads(payload)
    except json.decoder.JSONDecodeError:
        return on_fail("Invalid input: Not a JSON string")

    if "user_id" not in data:
        return on_fail("Invalid input: user_id missing")
    if "content" not in data:
        return on_fail("Invalid input: content missing")
    if "image" not in data:
        return on_fail("Invalid input: image missing")
    for i in data["image"]:
        if "filename" not in i or "file" not in i:
            return on_fail("Invalid input: Incorrect format in image field")

    user_id = data["user_id"]
    content = data["content"]
    image = data["image"]

    try:
        result = create_moment(user_id, content, image, image_collection, moment_collection)
    except TypeError as err:
        return on_fail(err)

    return on_success(result), 200


def on_success(data):
    return json.dumps(data), 200


def on_fail(error_message):
    data = {"status": "error", "message": error_message}
    return json.dumps(data), 400
