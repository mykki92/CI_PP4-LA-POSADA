from django.shortcuts import render
from django.views import generic, View
from django.contrib.auth.models import User
from django.contrib import messages
import datetime


# View to display the booking page
def booking(request):
    return render(request, 'booking/booking.html')
