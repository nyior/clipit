from django.urls import reverse
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
        cls.route = reverse("shorten-url")
        cls.payload = {
                            "longUrl": "https://nyior-clement.netlify.app/",
                            "shortcode": "xxbb5"
                        }
        client = Client.objects.create(client_id="xxy45")

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
        
        response = self.client.post(
                                    self.route, 
                                    self.payload, 
                                    format='json')
        request = response.wsgi_request

        client = get_or_create_client(request)

        self.assertTrue(isinstance(client, Client))
        

    def test_set_cookie(self):
        """tests that the set_cookie method sets the appropriate
        cookie on response"""

        response = self.client.post(
                                    self.route, 
                                    self.payload, 
                                    format='json')
        request = response.wsgi_request

        set_cookie(
                    request, 
                    response, 
                    self.client)

        self.assertContains(response, "clientId")