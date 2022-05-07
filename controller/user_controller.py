from bson import ObjectId
import json

from manager import user_manager


def set_user_activity(user_id, status, user_collection):
    return user_manager.set_active(user_collection, ObjectId(user_id), status)

def set_user_setting(user_collection, user_id, settings):
    return json.dumps(user_manager.set_settings(user_collection, ObjectId(user_id), settings))
