import unittest
from bson import ObjectId
import mongomock

from manager.user_manager import *
from dal.user_dal import *
from test.test_utils import drop_table


class UnitTesting(unittest.TestCase):
    def setUp(self):
        mongo_client = mongomock.MongoClient()
        self.database = mongo_client["CSE312"]
        self.user_collection = self.database["user"]

    def test_register(self):
        # Register a normal user
        test_user = json.loads(register(self.user[0][0], self.user[0][1], self.user[0][2], self.user_collection))
        self.assertTrue("user_id" in test_user.keys())
        test_id = test_user["user_id"]
        # test = self.user_collection.find_one({"_id": ObjectId(test_id)})
        # print(test)
        self.assertEqual(test_user, {"displayName": "howie", "user_id": test_id, "email": "howie@gmail.com"})

        # Register a repeated user
        test_user = json.loads(register(self.user[0][0], self.user[0][1], self.user[0][2], self.user_collection))
        self.assertEqual(test_user, {'status': 'Error', 'message': 'A account with this email already exist.'})

        # Register a user with wrong email
        test_user = json.loads(register(self.user[4][0], self.user[4][1], self.user[4][2], self.user_collection))
        self.assertEqual(test_user, {'status': 'Error', 'message': 'The email formmat is wrong.'})

        # Register a user with empty password
        test_user = json.loads(register(self.user[5][0], self.user[5][1], self.user[5][2], self.user_collection))
        self.assertEqual(test_user, {'status': 'Error', 'message': "password can't be empty"})

        message = drop_table(self.database, "user")
        self.assertTrue(message)

    def test_login(self):
        # Login as a non-exits user

        test_user = json.loads(login(self.user[6][1], self.user[6][2], self.user_collection))
        self.assertEqual(test_user, {'status': 'Error', 'message': 'User not found'})

        test_user = json.loads(register(self.user[0][0], self.user[0][1], self.user[0][2], self.user_collection))
        # Login as a exited user with all correct infor
        test_user = json.loads(login(self.user[0][1], self.user[0][2], self.user_collection))
        test_id = test_user["user_id"]
        self.assertEqual(test_user,
                         {"displayName": "howie", "user_id": test_id, "email": "howie@gmail.com", 'settings': '#1c5cbc'})

        # Login as a exited user with wrong password
        test_user = json.loads(login(self.user[3][1], self.user[3][2], self.user_collection))
        self.assertEqual(test_user, {'status': 'Error', 'message': 'User not found'})

        # Login as a exited user with wrong email
        test_user = json.loads(login(self.user[4][1], self.user[4][2], self.user_collection))
        self.assertEqual(test_user, {'status': 'Error', 'message': 'User not found'})

        # Login as a exited user with empty password
        test_user = json.loads(login(self.user[5][1], self.user[5][2], self.user_collection))
        self.assertEqual(test_user, {'status': 'Error', 'message': 'User not found'})

        # Login as a exited user with no email
        test_user = json.loads(login("", self.user[6][2], self.user_collection))
        self.assertEqual(test_user, {'status': 'Error', 'message': 'User not found'})

        message = drop_table(self.database, "user")
        self.assertTrue(message)

    def test_get_all(self):
        # Test when there is no user in database
        user_list = json.loads(get_all_user(self.user_collection))
        self.assertEqual(user_list, [])

        # Test when there is one user
        test_user1 = json.loads(register(self.user[0][0], self.user[0][1], self.user[0][2], self.user_collection))
        test_id1 = test_user1["user_id"]
        user_list = json.loads(get_all_user(self.user_collection))
        self.assertEqual(user_list,
                         [{"user_id": test_id1, "displayName": "howie", "email": "howie@gmail.com", "active": False}])

        # Test when there are more than one user, which are two users
        test_user2 = json.loads(register(self.user[1][0], self.user[1][1], self.user[1][2], self.user_collection))
        test_id2 = test_user2["user_id"]
        user_list = json.loads(get_all_user(self.user_collection))
        self.assertEqual(user_list,
                         [{'user_id': test_id1, 'displayName': 'howie', 'email': 'howie@gmail.com', "active": False},
                          {'user_id': test_id2, 'displayName': 'shouyue', 'email': 'shoouyue@email.com',
                           "active": False}])

        # Drop table at the end
        message = drop_table(self.database, "user")
        self.assertTrue(message)

    def test_set_active(self):
        # Set a non-existed user
        user_id_str = "4FAFEE7F4430C0696529710E"
        id = ObjectId(user_id_str)
        test_user1 = json.loads(set_active(self.user_collection, id, True))
        self.assertEqual(test_user1, {'status': 'Error', 'message': 'User account not found'})

        # set a inactive user to active
        test_user1 = json.loads(register(self.user[0][0], self.user[0][1], self.user[0][2], self.user_collection))
        test_id1 = test_user1["user_id"]
        updated_user = json.loads(set_active(self.user_collection, ObjectId(test_id1), True))
        self.assertEqual(updated_user, {'displayName': 'howie', 'email': 'howie@gmail.com',
                                        'active': True, 'user_id': test_id1})

        # set a active user to inactive
        updated_user = json.loads(set_active(self.user_collection, ObjectId(test_id1), False))
        self.assertEqual(updated_user, {'displayName': 'howie', 'email': 'howie@gmail.com',
                                        'user_id': test_id1, 'active': False})

        # Drop table at the end
        message = drop_table(self.database, "user")
        self.assertTrue(message)

    def test_set_settings(self):
        # Set a non-existed user
        user_id_str = "4FAFEE7F4430C0696529710E"
        id = ObjectId(user_id_str)
        test_user1 = set_settings(self.user_collection, id, "red")
        self.assertEqual(test_user1, {'status': False, 'message': 'User not found'})

        # set a user's settings to red
        test_user1 = json.loads(register(self.user[0][0], self.user[0][1], self.user[0][2], self.user_collection))
        test_id1 = test_user1["user_id"]
        updated_user = set_settings(self.user_collection, ObjectId(test_id1), "red")
        self.assertEqual(updated_user, {'status': True, 'message': {'displayName': 'howie', 'email': 'howie@gmail.com',
                                                                    'settings': 'red', 'user_id': test_id1}})

    def test_get_user_by_id(self):
        # Get a non-existed user
        user_id_str = "4FAFEE7F4430C0696529710E"
        id = ObjectId(user_id_str)
        test_user1 = json.loads(get_user_by_id(self.user_collection, id))
        self.assertEqual(test_user1, {'message': 'User not found', 'status': 'Error'})

        # Get a user
        test_user1 = json.loads(register(self.user[0][0], self.user[0][1], self.user[0][2], self.user_collection))
        test_id1 = test_user1["user_id"]
        test_user1 = json.loads(get_user_by_id(self.user_collection, ObjectId(test_id1)))
        self.assertEqual(test_user1, {'displayName': 'howie', 'email': 'howie@gmail.com',
                                      'user_id': test_id1, 'settings': '#1c5cbc'})

    def drop_table(self, database, table: str):
        if table in database.list_collection_names():
            expect_table = database[table]
            expect_table.drop()
            # message = "Table " + table + "dropped"
            return True
        else:
            error_message = "Table " + table + " doesn't exist"
        return error_message

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

    # wrong passowrd
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
