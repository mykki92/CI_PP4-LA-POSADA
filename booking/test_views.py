from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser
from django.utils import timezone
from .models import Booking
from .views import ViewBookings


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.make_booking_url = reverse('make_booking')
        self.booking_confirmed_url = reverse('booking_confirmed')

    def test_make_booking_GET(self):
        response = self.client.get(self.make_booking_url)

        self.assertEqual(response.status_code, 200)

    def test_booking_confirmed_GET(self):
        response = self.client.get(self.booking_confirmed_url)

        self.assertEqual(response.status_code, 200)


class ViewBookingsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.booking = Booking.objects.create(
            user=self.user, booking_date=timezone.now().date())

    def test_view_bookings_authenticated(self):
        url = reverse('view_bookings')
        request = self.factory.get(url)
        request.user = self.user

        response = ViewBookings.as_view()(request)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_bookings.html')
        self.assertContains(response, self.booking.booking_date)

    def test_view_bookings_unauthenticated(self):
        url = reverse('view_bookings')
        request = self.factory.get(url)
        request.user = AnonymousUser().id

        response = ViewBookings.as_view()(request)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('accounts:login'))
