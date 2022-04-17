import os

from pymongo import MongoClient


def connect_databases(collection_list):
    print("Connecting databases")

    mongo_url = get_mongo_url()
    mongo_client = MongoClient(mongo_url)
    db_list = {}

    for collection_name in collection_list:
        print("Connecting {}".format(collection_name))
        db_list[collection_name] = mongo_client["CSE312"][collection_name]

    # initialize_database(db_list)
    print("initialize_database success")
    print(db_list)
    return db_list


def get_mongo_url():
    env_url = os.getenv('MONGODB_URL')
    if env_url is None:
        return "mongo:27017"
    else:
        return os.getenv('MONGODB_URL')


if __name__ == '__main__':
    collection_list = ["user", "chat", "image", "moment"]
    db_list = connect_databases(collection_list)
