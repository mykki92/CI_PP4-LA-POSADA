from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import TapasItem


# Registration of the tapas items for the admin panel
@admin.register(TapasItem)
class TapasAdmin(SummernoteModelAdmin):
    list_display = ('tapas_name', 'tapas_type', 'price')
    search_fields = ('tapas_name', 'description')
    summernote_fields = ('description')
