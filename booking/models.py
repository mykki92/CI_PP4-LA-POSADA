from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


# class for the booking model
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    created_on = models.DateTimeField(auto_now_add=True)
    booking_date = models.DateField()
    booking_time = models.CharField(max_length=25, choices=time_slots)
    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE,
        related_name="table_reserved",
        null=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user",
        null=True
    )
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=200, default="")
    phone = PhoneNumberField(null=True)
    status = models.CharField(
        max_length=25,
        choices=status_options,
        default='awaiting confirmation'
    )
    seats = (
        (1, "1 Guest"),
        (2, "2 Guests"),
        (3, "3 Guests"),
        (4, "4 Guests"),
        (5, "5 Guests"),
        (6, "6 Guests"),
        (7, "7 Guests"),
        (8, "8 Guests"),
    )
    party_of = models.IntegerField(choices=seats, default=2)

    class Meta:
        ordering = ['-booking_time']
        unique_together = ('booking_date', 'booking_time', 'table')

    def __str__(self):
        return self.status
