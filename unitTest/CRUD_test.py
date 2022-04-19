import unittest
import mongomock

from manager import *
from user_CRUD import *

class UnitTesting(unittest.TestCase):
    def setUp(self):
        mongo_client = mongomock.MongoClient()
        self.image_collection = mongo_client["CSE312"]["user"]

    def testRegister(self):
        for i in range(5):
        print(register(user[i][0], user[i][1], user[i][2]))
    
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