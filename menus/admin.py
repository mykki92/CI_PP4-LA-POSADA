from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import TapasItem, DrinkItem


# Registration of the tapas items for the admin panel
@admin.register(TapasItem)
class TapasAdmin(SummernoteModelAdmin):
    list_display = (
        'tapas_name', 'tapas_type', 'tapas_price', 'plato_price', 'sides_price'
        )
    search_fields = ('tapas_name', 'description')
    summernote_fields = ('description')


# Registration of the drinks items for the admin panel
@admin.register(DrinkItem)
class DrinkAdmin(SummernoteModelAdmin):
    list_display = ('drink_name', 'drink_type', 'price')
    search_fields = ('drink_name', 'description')
    summernote_fields = ('description')
