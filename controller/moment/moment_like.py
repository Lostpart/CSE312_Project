import json

from manager.moment_manager import like_moment


def moment_like_controller(payload, moment_collection):
    if payload is None:
        return on_fail("Invalid input: No payload")

    moment_id = payload["moment_id"]

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
