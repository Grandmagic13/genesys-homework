import unittest
import requests
import json

from common import BASE_URL
from jsonschema import validate
from hamcrest import *

BASE64_ENDPOINT_URL = "{0}/{1}".format(BASE_URL, "base64")
HELLO_WORLD_ENCODED = "SGVsbG8gV29ybGQh"
HELLO_WORLD_DECODED = "Hello World!"


class Base64Tests(unittest.TestCase):
    # TODO test valid input -> expect correct decode
    # TODO test valid input -> expect status code 200
    # TODO test valid input -> expect valid schema
    # TODO test invalid input
    # TODO test invalid characters? any specials, whitespaces etc.
    # TODO test with empty input, expect erroneous response 404

    # def test_get_uuid_endpoint_returns_200_ok(self):
    #     response = requests.get(UUID_ENDPOINT_URL)
    #     assert_that(response.status_code, is_(200))
    #
    # def test_get_uuid_endpoint_schema_validity(self):
    #     schema = {
    #         "type": "object",
    #         "properties": {
    #             "uuid": {"type": "string"}
    #         }
    #     }
    #     response = requests.get(UUID_ENDPOINT_URL)
    #     json_data = json.loads(response.text)
    #     validate(instance=json_data, schema=schema)
    #     assert_that(json_data['uuid'], is_uuid())


if __name__ == '__main__':
    unittest.main()
