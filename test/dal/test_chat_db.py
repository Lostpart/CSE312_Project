import json
import unittest

import mongomock

from dal.chat_db import send_chat, chat_history


class MyTestCase(unittest.TestCase):

    def test_something(self):
        collection = mongomock.MongoClient()["test-chat_db"]
        collection = collection["test-chat_db"]
        collection.delete_many({})
        dict1 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013",
            "message": "leile",
            "image": None
        }
        send_chat(dict1, collection, False)
        self.assertEqual([dict1], json.loads(chat_history({"from": "123456789012123456789012","to": "123456789012123456789013"}, collection)))
        collection.delete_many({})
        dict3 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013",
            "message": "leile",
            "image": None
        }
        send_chat(dict3, collection, False)
        dict8 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789014",
            "message": "xinsuiing",
            "image": None
        }
        send_chat(dict8, collection, False)
        self.assertEqual([dict3], json.loads(chat_history({"from": "123456789012123456789012","to": "123456789012123456789013"}, collection)))  # add assertion here
        collection.delete_many({})


if __name__ == '__main__':
    unittest.main()
