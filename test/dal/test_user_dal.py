from lib2to3.pgen2.token import RPAR
import unittest
from bson import ObjectId
import mongomock

from dal.user_dal import *

class UnitTesting(unittest.TestCase):
    def setUp(self):
        mongo_client = mongomock.MongoClient()
        self.database = mongo_client["CSE312"]
        self.user_collection = self.database["user"]

    def test_create(self):
        # Test create a user with proper format
        # Inputs for create must be checked before passing arguments
        test_result = create(self.user_collection, self.user[0][0], self.user[0][1], self.user[0][2])
        self.assertEqual(test_result["displayName"], self.user[0][0])
        self.assertEqual(test_result["email"], self.user[0][1])
        self.assertTrue("user_id" in test_result.keys())
        self.assertTrue(test_result["user_id"] != "")
        message = drop_table(self.database, "user")
        self.assertTrue(message)

    def test_get_user(self):
        # Get a non-exist user by id
        test_result = get_user(self.user_collection, ObjectId("4FAFEE7F4430C0696529710E"))
        self.assertEqual(test_result, {'status': False, 'message': 'User not found'})

        # Get a non-exist user by email and password
        test_result = get_user(self.user_collection, self.user[0][1], self.user[0][2])
        self.assertEqual(test_result, {'status': False, 'message': 'User not found'})

        # Get a existed user by id
        temp_user = create(self.user_collection, self.user[0][0], self.user[0][1], self.user[0][2])
        test_id = ObjectId(temp_user["user_id"])
        test_result = get_user(self.user_collection, test_id)
        self.assertEqual(test_result, {'status': True, 'message': {'displayName': 'howie', 'email': 'howie@gmail.com', 'user_id': temp_user["user_id"]}})
        
        # Get a existed user by email and password
        test_result = get_user(self.user_collection, None, self.user[0][1], self.user[0][2])
        self.assertEqual(test_result, {'status': True, 'message': {'displayName': 'howie', 'email': 'howie@gmail.com', 'user_id': temp_user["user_id"]}})
        message = drop_table(self.database, "user")
        self.assertTrue(message)

    def test_update(self):
        # 说没用到所以不写先放着
        0

    def test_delete(self):
        # 说没用到所以不写先放着
        0

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

    # Wrong displayname
    username7 = " wrongdisplayname"
    email7 = "howie@gmail.com"
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