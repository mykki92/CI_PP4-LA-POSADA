from django.shortcuts import render
from django.views import generic, View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView
from django.core.paginator import Paginator
import datetime
from .models import Booking
from .forms import BookingForm


# Retrieves user information if user is signed in
def get_user(request):
    user_email = request.user.email
    user = User.objects.filter(email=user_email).first()
    return user


# Class to display the booking form and update the database with successful
# bookings
class MakeBooking(View):
    """
    Displays the booking form and auto fills the email field if the user
    is signed in
    """
    template_name = 'make_booking.html'
    success_message = 'Thats in the diary, well see you soon!'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            email = request.user.email
            booking_form = BookingForm(initial={'email': email})
        else:
            booking_form = BookingForm()
        return render(request, 'make_booking.html',
                      {'booking_form': booking_form})

    def post(self, request):
        """
        Checks that the provided information is valid and updates
        the database
        """
        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(
                request, "Booking successful, awaiting confirmation")

        return render(request, 'make_booking.html',
                      {'booking_form': booking_form})


# Class to display booking confirmation
class BookingConfirmed(generic.DetailView):
    template_name = 'bookings/booking_confirmed.html'

    def get(self, request):
        return render(request, 'bookings/booking_confirmed.html')
