import unittest
import mongomock

from manager.user_manager import *
from dal.user_dal import *

class UnitTesting(unittest.TestCase):
    def setUp(self):
        mongo_client = mongomock.MongoClient()
        self.user_collection = mongo_client["CSE312"]["user"]

    def test_register(self):
        # Register a normal user
        test_user = json.loads(register(self.user[0][0], self.user[0][1], self.user[0][2]))
        self.assertTrue("user_id" in test_user.keys())
        test_id = test_user["user_id"]
        self.assertEqual(test_user, {"displayName": "howie", "user_id": test_id, "email": "howie@gmail.com"})

        # Register a repeated user
        test_user = json.loads(register(self.user[0][0], self.user[0][1], self.user[0][2]))
        self.assertEqual(test_user, {'status': 'Error', 'message': 'A account with this email already exist.'})

        # Register a user with wrong email
        test_user = json.loads(register(self.user[4][0], self.user[4][1], self.user[4][2]))
        self.assertEqual(test_user, {'status': 'Error', 'message': 'The email formmat is wrong.'})

        # Register a user with empty password
        test_user = json.loads(register(self.user[5][0], self.user[5][1], self.user[5][2]))
        self.assertEqual(test_user, {'status': 'Error', 'message': "password can't be empty"})
        message = drop_table("user")
        self.assertTrue(message)

    def test_login(self):
        # Login as a non-exits user
        test_user = json.loads(login(self.user[6][1], self.user[6][2]))
        self.assertEqual(test_user, {'status': 'Error', 'message': 'User not found'})

        test_user = json.loads(register(self.user[0][0], self.user[0][1], self.user[0][2]))
        # Login as a exited user with all correct infor
        test_user = json.loads(login(self.user[0][1], self.user[0][2]))
        test_id = test_user["user_id"]
        self.assertEqual(test_user, {"displayName": "howie", "user_id": test_id, "email": "howie@gmail.com"})

        # Login as a exited user with wrong password
        test_user = json.loads(login(self.user[3][1], self.user[3][2]))
        self.assertEqual(test_user, {'status': 'Error', 'message': 'User not found'})

        # Login as a exited user with wrong email
        test_user = json.loads(login(self.user[4][1], self.user[4][2]))
        self.assertEqual(test_user, {'status': 'Error', 'message': 'User not found'})

        # Login as a exited user with empty password
        test_user = json.loads(login(self.user[5][1], self.user[5][2]))
        self.assertEqual(test_user, {'status': 'Error', 'message': 'User not found'})

        # Login as a exited user with no email
        test_user = json.loads(login("", self.user[6][2]))
        self.assertEqual(test_user, {'status': 'Error', 'message': 'User not found'})

        message = drop_table("user")
        self.assertTrue(message)

    # Corret part
    username1 = "howie"
    email1 = "howie@gmail.com"
    password1 = "haohuili"

    username2 = "shouyue"
    email2 = "shoouyue@email.com"
    password2 = "shiluo"

    username3 = "ywang298"
    email3 = "ywang298@email.com"
    password3 = "asbdkasb"

    # Wrong part

    #wrong passowrd
    username4 = "howie"
    email4 = "howie@gmail.com"
    password4 = "HaohuiLin"

    # Wrong email
    username5 = "wrongemail"
    email5 = "how ie@gmail.com"
    password5 = "HaohuiLin"

    # Empty password
    username6 = "empty password"
    email6 = "xpassword@gmail.com"
    password6 = ""

    # Wrong displayname. Current there is no regulation for username. Save for future
    username7 = " wrongdisplayname"
    email7 = "howi1e@gmail.com"
    password7 = "HaohuiLin"

    user = []
    user.append((username1, email1, password1))
    user.append((username2, email2, password2))
    user.append((username3, email3, password3))
    user.append((username4, email4, password4))
    user.append((username5, email5, password5))
    user.append((username6, email6, password6))
    user.append((username7, email7, password7))

if __name__ == '__main__':
    unittest.main()