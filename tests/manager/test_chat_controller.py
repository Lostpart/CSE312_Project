import json
import unittest
from chat.chat_controller import controller

class MyTestCase(unittest.TestCase):
    def test_something(self):
        dict1={"from":"123456789012123456789012", "to": "123456789012123456789013", "message": "leile"}
        a,b=controller(dict1)
        self.assertEqual(a, False)
        self.assertEqual(b,{'message': 'rawdata is not json format', 'status': 'error'})
        dict2 = {"from": "123456789012123456789012", "to": "123456789012123456789013", "message": "leile"}
        a, b = controller(json.dumps(dict2))
        self.assertEqual(a, False)
        self.assertEqual(b, {'message': 'rawdata is not json format', 'status': 'error'})

if __name__ == '__main__':
    unittest.main()
