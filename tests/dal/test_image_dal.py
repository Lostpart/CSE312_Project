import unittest
import mongomock
from dal.image_dal import *


class UnitTesting(unittest.TestCase):
    def setUp(self):
        mongo_client = mongomock.MongoClient()
        self.image_collection = mongo_client["CSE312"]["image"]

    def test_insert(self):
        image_id = insert(ObjectId("4FAFEE7F4430C0696529710E"), "test_filename_1", self.image_collection)
        image_id_str = str(image_id.inserted_id)
        self.assertEqual(image_id_str, str(get_by_str_id(image_id_str, self.image_collection)["_id"]))
        self.assertEqual(image_id_str, str(get_image_by_image_id(image_id.inserted_id, self.image_collection)["_id"]))


if __name__ == '__main__':
    unittest.main()
