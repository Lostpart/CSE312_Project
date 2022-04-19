import unittest
import mongomock

from dal.moment_dal import *


class UnitTesting(unittest.TestCase):
    def setUp(self):
        mongo_client = mongomock.MongoClient()
        self.moment_collection = mongo_client["CSE312"]["moment"]

    def test_insert(self):
        moment_id = insert(ObjectId("4FAFEE7F4430C0696529710E"), "test_moment1", [], self.moment_collection)
        moment_id_str = str(moment_id.inserted_id)

        self.assertEqual(moment_id_str, str(get_recent_moments(self.moment_collection)[0]["_id"]))


if __name__ == '__main__':
    unittest.main()
