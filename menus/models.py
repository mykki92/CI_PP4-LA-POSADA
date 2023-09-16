from django.db import models

# Food and drink categories
TAPAS_CATEGORY = ((0, 'Salads & Cold Cuts'), (1, 'Hot Dishes'), (2, 'Sides'))

# Model for tapas menu items


class TapasItem(models.Model):
    """
    a class for the tapas menu item model
    """
    tapas_id = models.AutoField(primary_key=True)
    tapas_name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200, unique=True)
    price = models.FloatField()
    tapas_type = models.IntegerField(choices=TAPAS_CATEGORY)

    class Meta:
        ordering = ['-tapas_type']

    def __str__(self):
        return self.tapas_name
