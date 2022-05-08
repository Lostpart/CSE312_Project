import unittest

import mongomock

from dal.chat_db import send_chat, get_data


class MyTestCase(unittest.TestCase):

    def test_something(self):
        collection = mongomock.MongoClient()["test-chat_db"]
        collection = collection["test-chat_db"]
        collection.delete_many({})
        dict1 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013",
            "message": "leile",
            "image": None,
        }
        send_chat(dict1, collection, False)
        result1 = get_data({"from": "123456789012123456789012","to": "123456789012123456789013"}, collection)
        result1[0].pop("_id")
        self.assertEqual([dict1], result1)
        collection.delete_many({})
        dict3 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013",
            "message": "leile",
            "image": None,
        }
        send_chat(dict3, collection, False)
        dict8 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789014",
            "message": "xinsuiing",
            "image": None
        }
        send_chat(dict8, collection, False)
        result3 = get_data({"from": "123456789012123456789012","to": "123456789012123456789013"}, collection)
        result3[0].pop("_id")
        self.assertEqual([dict3], result3)
        collection.delete_many({})


if __name__ == '__main__':
    unittest.main()
