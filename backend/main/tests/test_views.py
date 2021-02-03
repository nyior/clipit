from django.test import TestCase
from main.models import Url
from main.api.views import shorten_url

import reverse


class ShortenUrlView(TestCase):
    """ This tests the shorten url function"""

    @classmethod
    def setUpTestData(cls):
        """
        this method sets up the data to be used across 
        multiple methods"""
        global url
        url = Url.objects.create(
                                    long_url="https://nyior-clement.netlify.app/", 
                                    shortcode=None)

    def test_view_returns_status_ok(self):
        """tests if view always return an ok response"""
        route = reverse("shorten_url")
        resp = self.client.get(route)

        self.assertEqual(resp.status_code, 200)

    def test_view_returns_shortcode(self):
        """tests if shortcode is in the response returned"""
        route = reverse("shorten_url")
        resp = self.client.get(route)

        self.assertIn(url.shortcode, resp.content)

    def test_shortcode_isnot_null(self):
        """tests that the value of the shortcode returned is not null"""
        route = reverse("shorten_url")
        resp = self.client.get(route)

        self.assertTrue(url.shortcode is not None)