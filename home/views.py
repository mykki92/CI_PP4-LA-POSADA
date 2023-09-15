from django.shortcuts import render

# Create your views here.


def home(request):
    """
    a view to display the homepage
    """
    return render(request, 'home/index.html')
