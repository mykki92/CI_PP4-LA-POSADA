from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


# Choices for booking times
booking_slots = (
    ('12:00', '12:00'),
    ('13:00', '13:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
    ('16:00', '16:00'),
    ('17:00', '17:00'),
    ('18:00', '18:00'),
    ('19:00', '19:00'),
    ('20:00', '20:00'),
    ('21:00', '21:00'),
    ('22:00', '22:00'),
)

# Booking status categories
booking_status = (
    ('Pending', 'Pending'),
    ('Confirmed', 'Confirmed'),
    ('Rejected', 'Rejected'),
    ('Expired', 'Expired'),
)


# Class for the database table model
class Table(models.Model):
    table_id = models.AutoField(primary_key=True)
    table_number = models.CharField(max_length=25, unique=True)
    seats = models.IntegerField(default=2)

    class Meta:
        ordering = ['-seats']

    def ____(self):
        return self.table_number


# Class for the database booking model
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    created_on = models.DateTimeField(auto_now_add=True)
    booking_date = models.DateField()
    booking_time = models.CharField(max_length=25, choices=booking_slots)
    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE,
        related_name="table_booked",
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
        choices=booking_status,
        default='Pending'
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
