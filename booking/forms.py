from django import forms
from crispy_forms.helper import FormHelper
from datetime import datetime
from phonenumber_field.formfields import PhoneNumberField
from .models import Booking


class BookingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    booking_date = forms.DateField(widget=forms.DateInput(
            attrs={'type': 'date', 'min': datetime.now().date()}))

    phone = PhoneNumberField(widget=forms.TextInput())

    class Meta:
        model = Booking
        fields = (
            'name',
            'phone',
            'email',
            'party_of',
            'table',
            'booking_date',
            'booking_time')
