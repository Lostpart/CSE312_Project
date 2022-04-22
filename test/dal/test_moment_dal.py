import unittest
import mongomock

from dal.moment_dal import *


class UnitTesting(unittest.TestCase):
    def setUp(self):
        mongo_client = mongomock.MongoClient()
        self.moment_collection = mongo_client["CSE312"]["moment"]

    def test_insert(self):
        moment_id = insert(ObjectId("4FAFEE7F4430C0696529710E"), "test_moment1", [], self.moment_collection).inserted_id
        moment_id_str = str(moment_id)

        self.assertEqual(moment_id_str, str(get_recent_moments(self.moment_collection)[0]["_id"]))

    def test_recent_moment(self):
        moment_ids = []
        for i in range(0, 100):
            moment_ids.append(str(insert(ObjectId("4FAFEE7F4430C0696529710E"), "test_moment {}".format(i), [], self.moment_collection)
                              .inserted_id))

        recent_10_moments = get_recent_moments(self.moment_collection, limit=10)

        idx = 0
        for i in recent_10_moments:
            idx = idx + 1
            self.assertEqual(moment_ids[100 - idx], str(i["_id"]))
            self.assertEqual("test_moment {}".format(100 - idx), str(i["content"]))

    def test_like(self):
        moment_id = insert(ObjectId("4FAFEE7F4430C0696529710E"), "test_moment1", [], self.moment_collection).inserted_id

        self.assertEqual(0, get_recent_moments(self.moment_collection)[0]["like"])

        like_moment(moment_id, self.moment_collection)
        self.assertEqual(1, get_recent_moments(self.moment_collection)[0]["like"])

    def test_multiple_like(self):
        moment_id = insert(ObjectId("4FAFEE7F4430C0696529710E"), "test_moment1", [], self.moment_collection).inserted_id

        self.assertEqual(0, get_recent_moments(self.moment_collection)[0]["like"])

        for i in range(1000):
            like_moment(moment_id, self.moment_collection)
            if i % 50 == 0:
                self.assertEqual(i+1, get_recent_moments(self.moment_collection)[0]["like"])




if __name__ == '__main__':
    unittest.main()
