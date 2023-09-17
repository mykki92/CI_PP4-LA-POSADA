from django.shortcuts import render
from django.views import generic
from .models import TapasItem, DrinkItem


# View to display the tapas menu page
def tapas_menu(request):
    tapas_list = TapasItem.objects.all()
    return render(request, 'menus/tapas_menu.html', {'tapas_list': tapas_list})


# View to display the drink menu page
def drink_menu(request):
    drink_list = DrinkItem.objects.all()
    return render(request, 'menus/drink_menu.html', {'drink_list': drink_list})
