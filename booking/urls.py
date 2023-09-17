from django.urls import path
from booking import views

# url for the booking page
urlpatterns = [
    path('make_booking', views.MakeBooking.as_view(), name='make_booking'),
]
