from rest_framework.test import APITestCase
from main.api.utils import (
                            generate_shortcode, 
                            shortcode_is_valid,
                            get_or_create_client,
                            set_cookie)
from main.models import Url, Client


class UtilsTest(APITestCase):
    """ This tests the helper function defined in the utils file"""  

    @classmethod
    def setUpTestData(cls):
        """
        this method sets up the data to be used across 
        multiple classses"""

        cls.url = Url.objects.create(
                                    long_url="https://nyior-clement.netlify.app/",
                                    shortcode="xxbb5t") 

        cls.request = {
            "COOKIES": {
                "clientId": "xggh7"
            }
        }
        cls.invalid_request = {
            "COOKIES": {
               
            }
        }

    def test_generate_shortcode(self):
        """tests that the generate_shortcode function
        returns chars whose length == 6"""

        chars = generate_shortcode()

        self.assertEqual(len(chars), 6)

    def test_shortcode_isvalid(self):
        """fails if testcode is already exists or its length
        is less than 4"""

        self.assertFalse(shortcode_is_valid(self.url.shortcode))
        self.assertFalse(shortcode_is_valid("xxy"))

    def test_get_or_create_client(self):
        """tests that the get_or_create_client method
        always returns a client object"""

        client = get_or_create_client(self.request)
        client_2 = get_or_create_client(self.invalid_request)

        self.assertTrue(isinstance(client, Client))
        self.assertTrue(isinstance(client_2, Client))

    def test_set_cookie(self):
        """tests that the set_cookie method sets the appropriate
        cookie on response header"""

        client_id = self.request['COOKIES']['clientId']

        set_cookie(
                    self.invalid_request, 
                    self.invalid_request, 
                    client_id)

        self.assertContains(
                            self.invalid_request['COOKIES']['clientId'])
        self.assertEqual(
                          self.invalid_request['COOKIES']['clientId'])