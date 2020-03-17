from django.test import TestCase
from django.urls import reverse

from users.models import User
from users.views import login, logout, signup, accountlog


@classmethod
def test_data(self):
    self.user = User.objects.create_user(
        username = "test",
        email = "test@test.fr",
        password = "tests1",
    )
    self.user_profile = User(user=self.user)

def test_login(self):
    response = self.client.get(reverse('login'))
    self.assertEqual(response.status_code, 200)

def test_logout(self):
    response = self.client.get(reverse('logout'))
    self.assertEqual(response.status_code, 200)

def test_signup(self):
    response = self.client.get(reverse('signup'))
    self.assertEqual(response.status_code, 200)

def test_account(self):
    response = self.client.get(reverse('account'))
    self.assertEqual(response.status_code, 200)