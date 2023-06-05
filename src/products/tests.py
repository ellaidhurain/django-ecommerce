from django.test import TestCase
from django.contrib.auth import get_user_model

class URLTest(TestCase):
    def test_testhomepage(self):
        # self. client , is the built-in Django test client. This isn't a real browser, and doesn't even make real requests. It just constructs a Django HttpRequest object and passes it through the request/response process - middleware, URL resolver, view, template - and returns whatever Django produces
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
