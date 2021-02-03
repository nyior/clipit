from django.test import TestCase
from main.api.db_models import Url


class UrlModelTest(TestCase):
    """ This tests the Url model """

    @classmethod
    def setUpTestData(cls):
        """
        this method sets up the data to be used across 
        multiple methods"""
        url = Url.objects.create(
                                    long_url="https://nyior-clement.netlify.app/", 
                                    shortcode=None)

    def test_object_created(self):
        """tests if object has been created""" 
        self.assertTrue(isinstance(url, Url))

        #verifies that the model's save method does not save the 
        #shortcode as null, bu instead generates a shortcode
        self.asseretTrue(url.shortcode is not None)
        self.assertEqual(url.__unicode__(), url.shortcode)

    def test_raises_exception_for_invalid_urls(self):
        """sees if the classes raises an exception for invalid urls"""
        with self.assertRaises(Exception):
            Url.objects.create(
                                long_url="an invalid url", 
                                shortcode=None)

    def test_shortcode_is_shorter(self):
        """test that the generated short code is shorter than
        the original url"""
        self.assertLess(len(url.shortcode), len(url.long_url))

    def test_visited(self):
        """ test that visited function increases number of hits
        by 1"""
        hits = url.hits
        url.visited
        new_hits = url.visited()
        
        self.assertTrue((new_hits-hits) == 1)

        

    
