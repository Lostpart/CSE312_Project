import unittest
import mongomock
from dal.image_dal import *
from manager.image_manager import *


class UnitTesting(unittest.TestCase):

    def setUp(self):
        mongo_client = mongomock.MongoClient()
        self.image_collection = mongo_client["CSE312"]["image"]

    def test_insert(self):
        image_id_str = add_image_by_base64(self.user_id, self.image_base64, "jpg", self.image_collection)
        image_in_db = get_image_by_image_id(ObjectId(image_id_str), self.image_collection)
        self.assertEqual(str(image_id_str), str(image_in_db["_id"]))
        self.assertEqual(image_in_db["filename"], get_image_filename_by_image_id(ObjectId(image_id_str), self.image_collection))

    user_id_str = "4FAFEE7F4430C0696529710E"
    user_id = ObjectId(user_id_str)
    image_base64 = "/9j/4AAQSkZJRgABAQEAYABgAAD//gAUU29mdHdhcmU6IFNuaXBhc3Rl/9sAQwADAgIDAgIDAwMDBAMDBAUIBQUEBAUKBwcGC" \
                   "AwKDAwLCgsLDQ4SEA0OEQ4LCxAWEBETFBUVFQwPFxgWFBgSFBUU/9sAQwEDBAQFBAUJBQUJFA0LDRQUFBQUFBQUFBQUFBQUFB" \
                   "QUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQU/8AAEQgAEAAQAwEiAAIRAQMRAf/EAB8AAAEFAQEBAQEBAAAAAAA" \
                   "AAAABAgMEBQYHCAkKC//EALUQAAIBAwMCBAMFBQQEAAABfQECAwAEEQUSITFBBhNRYQcicRQygZGhCCNCscEVUtHwJDNicoIJ" \
                   "ChYXGBkaJSYnKCkqNDU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6g4SFhoeIiYqSk5SVlpeYmZqio6Slp" \
                   "qeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2drh4uPk5ebn6Onq8fLz9PX29/j5+v/EAB8BAAMBAQEBAQEBAQEAAAAAAA" \
                   "ABAgMEBQYHCAkKC//EALURAAIBAgQEAwQHBQQEAAECdwABAgMRBAUhMQYSQVEHYXETIjKBCBRCkaGxwQkjM1LwFWJy0QoWJDT" \
                   "hJfEXGBkaJicoKSo1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoKDhIWGh4iJipKTlJWWl5iZmqKjpKWm" \
                   "p6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uLj5OXm5+jp6vLz9PX29/j5+v/aAAwDAQACEQMRAD8A8qvtC1H+zxPFO" \
                   "w3SMm8xKoZtzJkPv2FTvc5zhdqgkk5pi6Vq94IEne3tGklZAImWRBhij5wSQVy3QEcfxD7uuILY2ko1GxnYSSSFZEaVlYqnzK" \
                   "wUjcuFyWAwXB+9tIMggEcsltera2sEdqiyTXAFz5ciMSr7sgKTwxAIUjA6hkr4rnZ9N/ZmDv8Aw1of/9k="

if __name__ == '__main__':
    unittest.main()
