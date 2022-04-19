import unittest
import requests
from bson import ObjectId

from feature.chat.chat_db import send_chat, chat_history


class MyTestCase(unittest.TestCase):
    path = 'http://127.0.0.1:8080/'

    def test_something(self):
        path = self.path + "test-sendchat"
        dict1 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013",
            "message": "leile",
            "image": None
        }
        requests.post(path, json=dict1)
        dict2 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013"
        }
        path = self.path + "test-getchat"
        a = requests.get(path, json=dict2)
        a = a.json()
        self.assertEqual(a, [{'from': '123456789012123456789012', 'to': '123456789012123456789013', 'message': 'leile', 'image': None}])  # add assertion here
        path = self.path + "test-sendchat"
        dict3 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013",
            "message": "leile",
            "image": None
        }
        requests.post(path, json=dict3)
        dict4 = {
            "from": "123456789012123456789013",
            "to": "123456789012123456789012",
            "message": "sheibushine",
            "image": None
        }
        requests.post(path, json=dict4)
        dict5 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013",
            "message": "xiangshuijiao",
            "image": None
        }
        requests.post(path, json=dict5)
        dict6 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013",
            "message": "woye",
            "image": None
        }
        requests.post(path, json=dict6)
        dict7 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013"
        }
        path = self.path + "test-getchat"
        a = requests.get(path, json=dict7)
        a = a.json()
        print(a)
        self.assertEqual(a, [{'from': '123456789012123456789012', 'to': '123456789012123456789013', 'message': 'leile', 'image': None}, {'from': '123456789012123456789013', 'to': '123456789012123456789012', 'message': 'sheibushine', 'image': None}, {'from': '123456789012123456789012', 'to': '123456789012123456789013', 'message': 'xiangshuijiao', 'image': None}, {'from': '123456789012123456789012', 'to': '123456789012123456789013', 'message': 'woye', 'image': None}])  # add assertion here
        path = self.path + "test-sendchat"
        dict3 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013",
            "message": "leile",
            "image": None
        }
        requests.post(path, json=dict3)
        dict4 = {
            "from": "123456789012123456789013",
            "to": "123456789012123456789012",
            "message": "sheibushine",
            "image": None
        }
        requests.post(path, json=dict4)
        dict8 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789014",
            "message": "xinsuiing",
            "image": None
        }
        requests.post(path, json=dict8)
        dict8 = {
            "from": "123456789012123456789019",
            "to": "123456789012123456789014",
            "message": "xinsuiing",
            "image": None
        }
        requests.post(path, json=dict8)
        dict5 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013",
            "message": "xiangshuijiao",
            "image": None
        }
        requests.post(path, json=dict5)
        dict6 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013",
            "message": "woye",
            "image": None
        }
        requests.post(path, json=dict6)
        dict7 = {
            "from": "123456789012123456789012",
            "to": "123456789012123456789013"
        }
        path = self.path + "test-getchat"
        a = requests.get(path, json=dict7)
        a = a.json()
        self.assertEqual(a, [
            {'from': '123456789012123456789012', 'to': '123456789012123456789013', 'message': 'leile', 'image': None},
            {'from': '123456789012123456789013', 'to': '123456789012123456789012', 'message': 'sheibushine',
             'image': None},
            {'from': '123456789012123456789012', 'to': '123456789012123456789013', 'message': 'xiangshuijiao',
             'image': None}, {'from': '123456789012123456789012', 'to': '123456789012123456789013', 'message': 'woye',
                              'image': None}])  # add assertion here


if __name__ == '__main__':
    unittest.main()
