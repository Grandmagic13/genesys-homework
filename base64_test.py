import unittest
import requests

from common import BASE_URL
from hamcrest import *

BASE64_ENDPOINT_URL = "{0}/{1}".format(BASE_URL, "base64")
HELLO_WORLD_ENCODED = "SGVsbG8gV29ybGQh"
HELLO_WORLD_DECODED = "Hello World!"
INVALID_INPUT = "as!da*sd"


class Base64Tests(unittest.TestCase):
    def test_get_base64_decode_for_valid_input_returns_200_ok(self):
        url = "{0}/{1}".format(BASE64_ENDPOINT_URL, HELLO_WORLD_ENCODED)
        response = requests.get(url)
        assert_that(response.status_code, is_(200))

    # endpoint returns 200 ok but with error message in body
    def test_get_base64_decode_for_invalid_input_without_special_characters_returns_200_ok(self):
        url = "{0}/{1}".format(BASE64_ENDPOINT_URL, INVALID_INPUT)
        response = requests.get(url)
        assert_that(response.status_code, is_(200))

    def test_get_base64_decode_for_empty_input_returns_404_not_found(self):
        url = "{0}/{1}".format(BASE64_ENDPOINT_URL, "")
        response = requests.get(url)
        assert_that(response.status_code, is_(404))

    def test_get_base64_decode_for_special_characters_input_returns_400_bad_request(self):
        url = "{0}/{1}".format(BASE64_ENDPOINT_URL, "!!!!%%%%%%%!!**")
        response = requests.get(url)
        assert_that(response.status_code, is_(400))

    def test_get_base64_decode_for_valid_input_returns_valid_body(self):
        url = "{0}/{1}".format(BASE64_ENDPOINT_URL, HELLO_WORLD_ENCODED)
        response = requests.get(url)
        assert_that(response.text, is_(HELLO_WORLD_DECODED))

    def test_get_base64_decode_for_invalid_input_returns_error_message_in_body(self):
        url = "{0}/{1}".format(BASE64_ENDPOINT_URL, INVALID_INPUT)
        response = requests.get(url)
        assert_that(response.text, contains_string("Incorrect Base64 data"))


if __name__ == '__main__':
    unittest.main()
