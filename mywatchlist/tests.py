from django.test import TestCase

from django.test import TestCase, Client
from django.test import TestCase

# Create your tests here.
class UrlTest(TestCase):
    def test_url_html(self):
        response=Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)
    
    def test_url_xml(self):
        response=Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)
    
    def test_url_json(self):
        response=Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)
# Create your tests here.
