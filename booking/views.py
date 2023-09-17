from django.shortcuts import render


# View to display the booking page
def booking(request):
    return render(request, 'booking/booking.html')
