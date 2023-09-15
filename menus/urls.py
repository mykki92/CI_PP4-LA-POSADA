from django.urls import path
from menus import views

# Urls for the food and drinks menu
urlpatterns = [
    path('', views.food_menu, name='food_menu'),
    path('', views.drink_menu, name='drink_menu'),
]
