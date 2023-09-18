from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('home.urls'), name='home_urls'),
    path('', include('menus.urls'), name='menus_urls'),
    path('', include('booking.urls'), name='booking_urls'),
    path('accounts/', include('allauth.urls')),
    path('', include('contact.urls')),
]
