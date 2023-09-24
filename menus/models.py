from django.db import models

# Food and drink categories
TAPAS_CATEGORY = (
    (0, 'Salads & Cold Cuts'),
    (1, 'Hot Dishes'),
    (2, 'Sides'),
    (3, 'Desserts')
)
DRINK_CATEGORY = (
    (0, 'Beers & Ciders'),
    (1, 'Wines & Sparkling'),
    (2, 'Cocktails'),
    (3, 'Spirits')
)


# Class for tapas menu item database model
class TapasItem(models.Model):
    """
    a class for the tapas menu item model
    """
    tapas_id = models.AutoField(primary_key=True)
    tapas_name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=400, blank=True)
    tapas_price = models.FloatField(default=0)
    plato_price = models.FloatField(default=0)
    sides_price = models.FloatField(default=0)
    dessert_price = models.FloatField(default=0)
    tapas_type = models.IntegerField(choices=TAPAS_CATEGORY)

    class Meta:
        ordering = ['-tapas_type']

    def __str__(self):
        return self.tapas_name


# Class for drink menu item database model
class DrinkItem(models.Model):
    """
    a class for the drink menu item model
    """
    drink_id = models.AutoField(primary_key=True)
    drink_name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200, blank=True)
    glass_price = models.FloatField(default=0)
    bottle_price = models.FloatField(default=0)
    drink_price = models.FloatField(default=0)
    drink_type = models.IntegerField(choices=DRINK_CATEGORY,)

    class Meta:
        ordering = ['-drink_type']

    def __str__(self):
        return self.drink_name
