import unittest
import mongomock

from manager.moment_manager import *


class UnitTesting(unittest.TestCase):
    def setUp(self):
        mongo_client = mongomock.MongoClient()
        self.moment_collection = mongo_client["CSE312"]["moment"]
        self.image_collection = mongo_client["CSE312"]["image"]

    def test_create_and_like(self):
        create_moment(self.user_id, self.moment_content_1, {}, self.image_collection,
                                      self.moment_collection)
        result = get_recent_moments(self.image_collection, self.moment_collection)[0]
        self.assertEqual(self.user_id_str, result["from"])
        self.assertEqual(self.moment_content_1, result["content"])
        self.assertEqual(0, result["like"])

        like_moment(result["moment_id"], self.moment_collection)

        result = get_recent_moments(self.image_collection, self.moment_collection)[0]
        self.assertEqual(1, result["like"])

    user_id_str = "4fafee7f4430c0696529710e"
    user_id = ObjectId(user_id_str)
    moment_content_1 = "test moment 1"


if __name__ == '__main__':
    unittest.main()
