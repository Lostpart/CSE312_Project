import json

from manager.moment_manager import like_moment


def moment_like_controller(payload, moment_collection):
    if payload is None:
        return on_fail("Invalid input: No payload")

    try:
        data = json.loads(payload)
    except json.decoder.JSONDecodeError:
        return on_fail("Invalid input: Not a JSON string")

    moment_id = data["moment_id"]

    try:
        db_result = like_moment(moment_id, moment_collection)
    except LookupError as err:
        return on_fail(err)

    result = {"moment_id": str(db_result["_id"]), "like": int(db_result["like"])}

    return on_success(result)


def on_success(data):
    return json.dumps(data)


def on_fail(error_message):
    raise ValueError(error_message)
