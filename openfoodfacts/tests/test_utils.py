from django.test import TestCase
from django.urls import reverse

from openfoodfacts.utils import get_json


class TestUtils(TestCase):

    def test_utils(self):
        base_url = 'https://fr.openfoodfacts.org/cgi/search.pl'
        