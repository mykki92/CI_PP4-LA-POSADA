from django.test import TestCase
from .models import TapasItem, DrinkItem


class TestModels(TestCase):

    def test_new_food(self):
        food = TapasItem.objects.create(
            tapas_name='Test Food',
            description='Test description',
            tapas_price='5',
            plato_price='10',
            tapas_type='0'
            )
        self.assertEqual(food.tapas_price, '5')
        self.assertEqual(food.plato_price, '10')
        self.assertEqual(food.description, 'Test description')
        self.assertEqual(food.tapas_type, '0')

    def test_new_drink(self):
        drink = DrinkItem.objects.create(
            drink_name='Test drink',
            description='Test description',
            drink_price='9.99',
            drink_type='0'
            )
        self.assertEqual(drink.drink_price, '9.99')
        self.assertEqual(drink.description, 'Test description')
        self.assertEqual(drink.drink_type, '0')
