from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ContactForm


# Retrieves user information if user is signed in
def get_user(request):
    user_email = request.user.email
    user = User.objects.filter(email=user_email).first()
    return user


# Class to display the contact form
class UserMessage(View):
    template_name = 'contact_us.html'
    success_message = 'Your message has been sent.'

    def get(self, request, *args, **kwargs):
        """
        Retrieves users email and inputs into email input
        """
        if request.user.is_authenticated:
            email = request.user.email
            contact_form = ContactForm(initial={'email': email})
        else:
            contact_form = ContactForm()
        return render(request, 'contact_us.html',
                      {'contact_form': contact_form})

    def post(self, request):
        """
        Checks that the provided information is valid and updates
        the database
        """
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.success(
                request, "Your message has been sent")
            return render(request, 'message_recieved.html')

        return render(request, 'contact_us.html',
                      {'contact_form': contact_form})
