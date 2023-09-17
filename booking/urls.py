from django.urls import path
from booking import views

# url for the booking page
urlpatterns = [
    path('booking', views.booking, name="booking"),
]
