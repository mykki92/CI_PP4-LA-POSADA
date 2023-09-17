from django.urls import path
from . import views

# url for the booking page
urlpatterns = [
    path('', views.booking, name="booking"),
]
