from django.urls import path
from contact import views


# url patterns for the contact page
urlpatterns = [
    path('contact/', views.UserMessage.as_view(), name='contact'),
]
