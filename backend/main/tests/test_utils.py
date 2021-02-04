from rest_framework.test import APITestCase
from main.api.utils import generate_shortcode, shortcode_is_valid
from main.models import Url


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