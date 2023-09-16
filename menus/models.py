from django.db import models

# Food and drink categories
TAPAS_CATEGORY = ((0, 'Salads & Cold Cuts'), (1, 'Hot Dishes'), (2, 'Sides'))
DRINK_CATEGORY = ((0, 'Beers'), (1, 'Wines'), (2, 'Cocktails'))


# Model for tapas menu items
class TapasItem(models.Model):
    """
    a class for the tapas menu item model
    """
    tapas_id = models.AutoField(primary_key=True)
    tapas_name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200, unique=True, blank=True)
    tapas_price = models.FloatField(default=0)
    plato_price = models.FloatField(default=0)
    sides_price = models.FloatField(default=0)
    tapas_type = models.IntegerField(choices=TAPAS_CATEGORY)

    class Meta:
        ordering = ['-tapas_type']

    def __str__(self):
        return self.tapas_name


# Model for drink menu items
class DrinkItem(models.Model):
    """
    a class for the drink menu item model
    """
    drink_id = models.AutoField(primary_key=True)
    drink_name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200, unique=True, blank=True)
    price = models.FloatField()
    drink_type = models.IntegerField(choices=DRINK_CATEGORY,)

    class Meta:
        ordering = ['-drink_type']

    def __str__(self):
        return self.drink_name
