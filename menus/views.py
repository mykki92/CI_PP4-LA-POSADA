from django.shortcuts import render

# Create your views here.


def get_food_menu(request):
    return render(request, 'menus/food_menu.html')
