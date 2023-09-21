from django.shortcuts import render, reverse, redirect
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


# Class to display the booking form
class MakeBooking(View):
    """
    Displays the booking form and auto fills the email field if the user
    is signed in
    """
    template_name = 'make_booking.html'
    success_message = 'Its a date! Well see you soon!'

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
            return render(request, 'booking_confirmed.html')

        return render(
            request, 'make_booking.html', {'booking_form': booking_form}
        )


# Class to display booking confirmation
class BookingConfirmed(generic.DetailView):
    template_name = 'booking/booking_confirmed.html'

    def get(self, request):
        return render(request, 'booking/booking_confirmed.html')


# Class to display a users current and past bookings
class ViewBookings(generic.ListView):
    model = Booking
    queryset = Booking.objects.filter().order_by('-created_on')
    template_name = 'view_bookings.html'
    paginated_by = 4

    def get(self, request, *args, **kwargs):
        booking = Booking.objects.all()
        paginator = Paginator(Booking.objects.filter(user=request.user), 4)
        page = request.GET.get('page')
        booking_page = paginator.get_page(page)
        today = datetime.datetime.now().date()

        for date in booking:
            if date.booking_date < today:
                date.status = 'Expired'

        if request.user.is_authenticated:
            bookings = Booking.objects.filter(user=request.user)
            return render(
                request,
                'view_bookings.html',
                {
                    'booking': booking,
                    'bookings': bookings,
                    'booking_page': booking_page})
        else:
            return redirect('accounts/login.html')


# Class to display options to change an existing booking
class AmendBooking(SuccessMessageMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'amend_booking.html'
    success_message = 'Booking has been amended.'

    def get_success_url(self, **kwargs):
        return reverse('view_bookings')


# Function to delete the selected booking by identifying its primary key
def cancel_booking(request, pk):
    booking = Booking.objects.get(pk=pk)

    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Booking cancelled")
        return redirect('view_bookings')
    else:
        return render(
            request, 'cancel_booking.html', {'booking': booking})
