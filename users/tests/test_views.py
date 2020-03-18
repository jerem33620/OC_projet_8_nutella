from django.test import TestCase
from django.urls import reverse

from users.models import User
from users.views import login, logout, signup, accountlog


class TestUsersPageTestCase(TestCase):

    def test_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_signup(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_accountlog(self):
        response = self.client.get(reverse('accountlog'))
        self.assertEqual(response.status_code, 200)