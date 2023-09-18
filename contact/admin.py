from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from .models import ContactUs


# Registration of contact model in the admin panel
@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    list_filter = (
        'user',
        'name',
        'email',
        'phone',
        'message_date'
    )
    list_display = (
        'message_id',
        'user',
        'name',
        'message',
        'phone',
        'message_date'
    )

    search_fields = ['name']
    list_filter = (('message_date', DateRangeFilter),)
