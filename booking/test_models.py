from django.test import TestCase
from datetime import date
from .models import Table, Booking, User


class TestModels(TestCase):

    def setUp(self):
        self.table = Table(table_id=1, table_number='Table 1', seats=2)
        self.user = User(
            username='Tester Test',
            email='test@aaa.com'
            )
        self.booking = Booking(
            booking_id=32,
            table=self.table,
            user=self.user,
            party_of=2,
            created_on='2023-12-12',
            booking_date='2023-12-12',
            booking_time='12:00',
            status='awaiting confirmation',
            name='Tester Test',
            phone='+353123456789',
            email='test@aaa.com',
            )

    def test_make_booking(self):
        self.assertEqual(self.booking.name, 'Tester Test')
        self.assertEqual(self.booking.booking_id, 32)
        self.assertEqual(self.booking.booking_date, '2023-12-12')
        self.assertEqual(self.booking.booking_time, '12:00')
        self.assertEqual(self.booking.party_of, 6)
        self.assertEqual(self.booking.status, 'awaiting confirmation')
        self.assertEqual(self.booking.name, 'Tester Test')
        self.assertEqual(self.booking.phone, '+353123456789')
        self.assertEqual(self.booking.email, 'test@aaa.com')
