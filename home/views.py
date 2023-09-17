from django.shortcuts import render


# View to display the homepage
def home(request):
    return render(request, 'home/index.html')
