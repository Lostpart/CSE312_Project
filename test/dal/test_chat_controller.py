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
        a = answer1["a"]
        b = answer1["b"]
        self.assertEqual(a, False)
        self.assertEqual(b, {'status': 'error', 'message': 'rawdata is not json format'})
        dict2 = {
            "from": "123456789012123456789012",
            "message": "leile"
        }
        answer2 = requests.post(self.path, json=dict2)
        answer2 = answer2.json()
        a = answer2["a"]
        b = answer2["b"]
        self.assertEqual(a, False)
        self.assertEqual(b, {'status': 'error', 'message': "'to' is not exists"})
        dict3 = {
            "from": "123456789012123456789012",
            "to": "1234567890",
            "message": "leile"
        }
        answer3 = requests.post(self.path, json=dict3)
        answer3 = answer3.json()
        a = answer3["a"]
        b = answer3["b"]
        self.assertEqual(a, False)
        self.assertEqual(b, {'status': 'error', 'message': 'to is not consistent with ObjectId format'})
        dict4 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013",
            "message": "leile"
        }
        answer4 = requests.post(self.path, json=dict4)
        answer4 = answer4.json()
        print(answer4)
        a = answer4["a"]
        b = answer4["b"]
        self.assertEqual(a, True)
        self.assertEqual(b, {'response': {
            'message': {'from': '123456789012123456789012', 'message': 'leile', 'to': '123456789012123456789013'},
            'status': True}, 'to': '123456789012123456789013'})


if __name__ == '__main__':
    unittest.main()
