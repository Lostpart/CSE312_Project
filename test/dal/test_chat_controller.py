import json
import unittest
import requests
from chat import chat_controller


class MyTestCase(unittest.TestCase):

    def test_something(self):
        dict1 = {"from": "123456789012123456789012", "to": "123456789012123456789013", "message": "leile"}
        a, b = chat_controller.controller(dict1)
        self.assertEqual(b, {'status': 'error', 'message': 'rawdata is not json format'})
        dict2 = {
            "from": "123456789012123456789012",
            "message": "leile"
        }
        a, b = chat_controller.controller(json.dumps(dict2))
        self.assertEqual(b, {'status': 'error', 'message': "'to' is not exists"})
        dict3 = {
            "from": "123456789012123456789012",
            "to": "1234567890",
            "message": "leile"
        }
        a, b = chat_controller.controller(json.dumps(dict3))
        self.assertEqual(b, {'status': 'error', 'message': 'to is not consistent with ObjectId format'})
        dict4 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013",
            "message": "leile"
        }
        a, b = chat_controller.controller(json.dumps(dict4))
        print(b)
        self.assertEqual(b["response"], {'message': {'from': '123456789012123456789012', 'message': 'leile', 'to': '123456789012123456789013'},
            'status': True})


if __name__ == '__main__':
    unittest.main()
