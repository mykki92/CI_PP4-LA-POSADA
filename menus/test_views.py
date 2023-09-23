from django.test import TestCase, Client
from django.urls import reverse


class TestMenusViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.tapas_menu_url = reverse('tapas_menu')
        self.drink_menu_url = reverse('drink_menu')

    def test_tapas_menu_GET(self):
        response = self.client.get(self.tapas_menu_url)

        self.assertEqual(response.status_code, 200)

    def test_drink_menu_GET(self):
        response = self.client.get(self.drink_menu_url)

        self.assertEqual(response.status_code, 200)
