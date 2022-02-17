import unittest
import requests
import json

from common import BASE_URL
from jsonschema import validate
from hamcrest import *

from uuid_matcher import is_uuid

UUID_ENDPOINT_URL = "{0}/{1}".format(BASE_URL, "uuid")


class UUIDTests(unittest.TestCase):
    def test_get_uuid_endpoint_returns_200_ok(self):
        response = requests.get(UUID_ENDPOINT_URL)
        assert_that(response.status_code, is_(200))

    def test_get_uuid_endpoint_schema_validity(self):
        schema = {
            "type": "object",
            "properties": {
                "uuid": {"type": "string"}
            }
        }
        response = requests.get(UUID_ENDPOINT_URL)
        json_data = json.loads(response.text)
        validate(instance=json_data, schema=schema)
        assert_that(json_data['uuid'], is_uuid())


if __name__ == '__main__':
    unittest.main()
