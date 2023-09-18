from django import forms
from crispy_forms.helper import FormHelper
from phonenumber_field.formfields import PhoneNumberField
from .models import ContactUs


class ContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    phone = PhoneNumberField(widget=forms.TextInput())

    class Meta:
        model = ContactUs
        fields = (
            'name',
            'phone',
            'email',
            'message'
        )
