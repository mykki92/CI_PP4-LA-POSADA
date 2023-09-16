from django.urls import path
from menus import views

# Urls for the food and drinks menu
urlpatterns = [
    path('tapas_menu', views.tapas_menu, name='tapas_menu'),
    path('drink_menu', views.drink_menu, name='drink_menu'),
]
