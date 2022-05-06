from bson import ObjectId

from manager import user_manager


def set_user_activity(user_id, status, user_collection):
    return user_manager.set_active(user_collection, ObjectId(user_id), status)
