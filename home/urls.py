from django.urls import path
from . import views

# url for the home page
urlpatterns = [
    path('', views.home, name="home"),
]
