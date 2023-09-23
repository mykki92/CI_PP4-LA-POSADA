from django.test import SimpleTestCase
from django.urls import reverse, resolve
from booking.views import (
    MakeBooking, ViewBookings, BookingConfirmed, AmendBooking, cancel_booking)


class TestBookingUrls(SimpleTestCase):

    def test_make_booking_resolved(self):
        url = reverse('make_booking')
        self.assertEquals(resolve(url).func.view_class, MakeBooking)

    def test_booking_confirmed_resolved(self):
        url = reverse('booking_confirmed')
        self.assertEquals(resolve(url).func.view_class, BookingConfirmed)

    def test_view_bookings_resolved(self):
        url = reverse('view_bookings')
        self.assertEquals(resolve(url).func.view_class, ViewBookings)

    def test_amend_booking_url_resolved(self):
        url = reverse('amend_booking', args=['1'])
        self.assertEquals(resolve(url).func.view_class, AmendBooking)

    def test_cancel_booking_url_resolved(self):
        url = reverse('cancel_booking', args=['1'])
        self.assertEquals(resolve(url).func, cancel_booking)
