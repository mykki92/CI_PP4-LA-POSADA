from django.shortcuts import render
from django.views import generic


# Create your views here.


def food_menu(request):
    return render(request, 'menus/food_menu.html')


def drink_menu(request):
    return render(request, 'menus/drink_menu.html')
