from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.decorators import login_required


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.make_booking_url = reverse('make_booking')
        self.booking_confirmed_url = reverse('booking_confirmed')
        self.view_bookings_url = reverse('view_bookings')

    def test_make_booking_GET(self):
        response = self.client.get(self.make_booking_url)

        self.assertEqual(response.status_code, 200)

    def test_booking_confirmed_GET(self):
        response = self.client.get(self.booking_confirmed_url)

        self.assertEqual(response.status_code, 200)

    @login_required
    def test_view_bookings_GET(self):
        response = self.client.get(self.view_bookings_url)

        self.assertEqual(response.status_code, 200)
