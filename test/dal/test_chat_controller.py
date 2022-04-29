import json
import unittest
import requests
from chat import chat_controller


class MyTestCase(unittest.TestCase):
    path = 'http://127.0.0.1:8080/test-controller'

    def test_something(self):
        dict1 = {"from": "123456789012123456789012", "to": "123456789012123456789013", "message": "leile"}
        answer1 = requests.post(self.path, dict1)
        answer1 = answer1.json()
        self.assertEqual(answer1, {'status': 'error', 'message': 'rawdata is not json format'})
        dict2 = {
            "from": "123456789012123456789012",
            "message": "leile"
        }
        answer2 = requests.post(self.path, json=dict2)
        answer2 = answer2.json()
        self.assertEqual(answer2, {'status': 'error', 'message': "'to' is not exists"})
        dict3 = {
            "from": "123456789012123456789012",
            "to": "1234567890",
            "message": "leile"
        }
        answer3 = requests.post(self.path, json=dict3)
        answer3 = answer3.json()
        self.assertEqual(answer3, {'status': 'error', 'message': 'to is not consistent with ObjectId format'})
        dict4 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013",
            "message": "leile"
        }
        answer4 = requests.post(self.path, json=dict4)
        answer4 = answer4.json()
        print(answer4)
        self.assertEqual(answer4, {'message': {'from': '123456789012123456789012', 'message': 'leile', 'to': '123456789012123456789013'},
            'status': True})


if __name__ == '__main__':
    unittest.main()
