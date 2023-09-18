from django.urls import path
from booking import views

# url patterns for the booking page
urlpatterns = [
    path('make_booking', views.MakeBooking.as_view(), name='make_booking'),
    path(
        'booking_confirmed/<int:pk>',
        views.BookingConfirmed.as_view(),
        name='booking_confirmed'
        ),
]
