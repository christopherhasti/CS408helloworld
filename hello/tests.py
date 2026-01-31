# hello/tests.py
from django.test import SimpleTestCase
from django.urls import reverse

class HelloWorldTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_content(self):
        response = self.client.get('/')
        self.assertContains(response, 'Hello World from Django')