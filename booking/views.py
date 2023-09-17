from django.shortcuts import render
from django.views import generic


# View to display the booking page
def booking(request):
    return render(request, 'booking/booking.html')
