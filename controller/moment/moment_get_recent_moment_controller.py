import json

from manager.moment_manager import get_recent_moments


def get_recent_moments_controller(payload, image_collection, moment_collection):
    if payload is None:
        return on_fail("Invalid input: No payload")

    limit = 100

    try:
        data = json.loads(payload)
    except json.decoder.JSONDecodeError:
        return on_fail("Invalid input: Not a JSON string")

    if "limit" in data:
        limit = data["limit"]

    result = get_recent_moments(image_collection, moment_collection, limit=limit)

    return on_success(result)


def on_success(data):
    return json.dumps(data), 200


def on_fail(error_message):
    data = {"status": "error", "message": error_message}
    return json.dumps(data), 400
