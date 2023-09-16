from django.shortcuts import render
from django.views import generic
from .models import TapasItem


# View for the tapas menu page
def tapas_menu(request):
    tapas_list = TapasItem.objects.all()
    return render(request, 'menus/tapas_menu.html', {'tapas_list': tapas_list})


def drink_menu(request):
    return render(request, 'menus/drink_menu.html')
