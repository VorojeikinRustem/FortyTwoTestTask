from django.test import TestCase, Client
from django.http import HttpRequest
from models import MyProfile


class ProfileTestCase(TestCase):
    def setUp(self):
        MyProfile.objects.create(
            name = 'Vova',
            last_name = 'Ivanov',
            date_of_birth = '1992-12-27',
            email = 'vova@mail.ru',
            skype = 'vova',
            bio = 'pass',
            other_contacts = 'vova@gmail.com'
        )

    def test_profile(self):
        vova = MyProfile.objects.get(name="Vova")
        self.assertEqual(vova.full_name(), 'Vova Ivanov')


    def test_http_response(self):
        response = self.client.get('/http_requests/')
        self.assertEqual(response.status_code, 200)
