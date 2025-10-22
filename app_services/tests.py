from django.test import TestCase
from rest_framework.test import  APITestCase
from rest_framework import  status
class HelloAPiTestcase(APITestCase):
    def test_hello_api(self):
        response = self.client.request('api/hello/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,{"maessage: Hello, World"})


# Create your tests here.
