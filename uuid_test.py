import unittest

from common import BASE_URL
from hamcrest import *
import requests

UUID_ENDPOINT_URL = "{0}/{1}".format(BASE_URL, "uuid")

class UUIDTests(unittest.TestCase):
    def test_get_uuid_endpoint_returns_200_ok(self):
        response = requests.get(UUID_ENDPOINT_URL)
        assert_that(response.status_code, is_(200))

    # test response body contains uuid

if __name__ == '__main__':
    unittest.main()
