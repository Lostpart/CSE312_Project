import json
import unittest
import requests
from bson import ObjectId
from dal.connect_database import connect_databases
from dal.chat_db import send_chat, chat_history


class MyTestCase(unittest.TestCase):

    def test_something(self):
        collection = connect_databases(["test-chat"])
        collection = collection["test-chat"]
        collection.delete_many({})
        dict1 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013",
            "message": "leile"
        }
        send_chat(dict1, collection, False)
        dict2 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013"
        }
        a = chat_history(dict2, collection)
        a = json.loads(a)
        self.assertEqual(a, [{'from': '123456789012123456789012', 'to': '123456789012123456789013', 'message': 'leile', 'image': None}])  # add assertion here
        collection.delete_many({})
        dict3 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013",
            "message": "leile"
        }
        send_chat(dict3, collection, False)
        dict4 = {
            "from": "123456789012123456789013",
            "to": "123456789012123456789012",
            "message": "sheibushine",
            "image": None
        }
        send_chat(dict4, collection, False)
        dict5 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013",
            "message": "xiangshuijiao",
            "image": None
        }
        send_chat(dict5, collection, False)
        dict6 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013",
            "message": "woye",
            "image": None
        }
        send_chat(dict6, collection, False)
        dict7 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013"
        }
        a = chat_history(dict7, collection)
        a = json.loads(a)
        print(a)
        self.assertEqual(a, [{'from': '123456789012123456789012', 'to': '123456789012123456789013', 'message': 'leile', 'image': None}, {'from': '123456789012123456789013', 'to': '123456789012123456789012', 'message': 'sheibushine', 'image': None}, {'from': '123456789012123456789012', 'to': '123456789012123456789013', 'message': 'xiangshuijiao', 'image': None}, {'from': '123456789012123456789012', 'to': '123456789012123456789013', 'message': 'woye', 'image': None}])  # add assertion here
        collection.delete_many({})
        dict3 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013",
            "message": "leile",
            "image": None
        }
        send_chat(dict3, collection, False)
        dict4 = {
            "from": "123456789012123456789013",
            "to": "123456789012123456789012",
            "message": "sheibushine",
            "image": None
        }
        send_chat(dict4, collection, False)
        dict8 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789014",
            "message": "xinsuiing",
            "image": None
        }
        send_chat(dict8, collection, False)
        dict8 = {
            "from": "123456789012123456789019",
            "to": "123456789012123456789014",
            "message": "xinsuiing",
            "image": None
        }
        send_chat(dict8, collection, False)
        dict5 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013",
            "message": "xiangshuijiao",
            "image": None
        }
        send_chat(dict5, collection, False)
        dict6 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013",
            "message": "woye",
            "image": None
        }
        send_chat(dict6, collection, False)
        dict7 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013"
        }
        a = chat_history(dict7, collection)
        a = json.loads(a)
        self.assertEqual(a, [
            {'from': '123456789012123456789012', 'to': '123456789012123456789013', 'message': 'leile', 'image': None},
            {'from': '123456789012123456789013', 'to': '123456789012123456789012', 'message': 'sheibushine',
             'image': None},
            {'from': '123456789012123456789012', 'to': '123456789012123456789013', 'message': 'xiangshuijiao',
             'image': None}, {'from': '123456789012123456789012', 'to': '123456789012123456789013', 'message': 'woye',
                              'image': None}])  # add assertion here
        collection.delete_many({})

if __name__ == '__main__':
    unittest.main()