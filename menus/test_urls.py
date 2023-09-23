from django.test import SimpleTestCase
from django.urls import reverse, resolve
from menus.views import tapas_menu, drink_menu


class TestMenusUrls(SimpleTestCase):
    def test_tapas_menu_resolved(self):
        url = reverse('tapas_menu')
        self.assertEquals(resolve(url).func, tapas_menu)

    def test_drink_menu_resolved(self):
        url = reverse('drink_menu')
        self.assertEquals(resolve(url).func, drink_menu)
