from django.shortcuts import render
from django.views import generic


# Create your views here.


def tapas_menu(request):
    return render(request, 'menus/tapas_menu.html')


def drink_menu(request):
    return render(request, 'menus/drink_menu.html')
