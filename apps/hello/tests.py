from django.test import TestCase

# Create your tests here.

from django.http import HttpRequest

class SomeTests(TestCase):

    def test_page_profile(self):
        request = HttpRequest()
        response = index(request)
        self.assertTrue(response.content.startswith(b'<html>')) 
        self.assertIn(b'<title>42 Coffee Cups Test Assignment</title>', response.content) 
        self.assertTrue(response.content.endswith(b'</html>'))  
