from django.test import TestCase
from django.urls import reverse

from favorites.views import favorite_list, favorite_save


class TestFavoritesPageTestCase(TestCase):
    def test_favorite_list_page(self):
        response = self.client.get(reverse('favorite_list'))
        self.assertEqual(response.status_code, 302)

    def test_favorite_save_page(self):
        response = self.client.get(reverse('favorite_save'))
        self.assertEqual(response.status_code, 302)