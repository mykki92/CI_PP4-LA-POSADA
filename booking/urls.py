from django.urls import path
from booking import views

# url patterns for the booking page
urlpatterns = [
    path('make_booking', views.MakeBooking.as_view(), name='make_booking'),
    path(
        'booking_confirmed',
        views.BookingConfirmed.as_view(),
        name='booking_confirmed'
    ),
    path('view_bookings', views.ViewBookings.as_view(), name='view_bookings'),
    path(
        'amend_booking',
        views.AmendBooking.as_view(),
        name='amend_booking'
    ),
]
