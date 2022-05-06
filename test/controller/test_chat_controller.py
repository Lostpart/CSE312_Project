import json
import unittest

import mongomock

from controller import chat_controller
from dal.connect_database import connect_databases


class MyTestCase(unittest.TestCase):

    def test_something(self):
        collection = mongomock.MongoClient()["test-chat_controller"]
        collection = collection["test-chat_controller"]
        collection.delete_many({})
        dict2 = {
            "from": "123456789012123456789012",
            "message": "leile"
        }
        a, b = chat_controller.controller(dict2, collection)
        self.assertEqual(b["status"], "error")
        dict4 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013",
            "message": "leile"
        }
        a, b = chat_controller.controller(dict4, collection)
        print(b)
        self.assertEqual(b["response"], {'message': dict4, 'status': True})


if __name__ == '__main__':
    unittest.main()
