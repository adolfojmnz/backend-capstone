from django.test import TestCase

from ..models import Menu
from .mixins import CreateMenuItemsMixin


class MenuTest(CreateMenuItemsMixin, TestCase):

    def setUp(self):
        self.create_menu_items()

    def test_created_items(self):
        for idx in self.items.keys():
            inventory = 5 if self.items[idx].get('inventory') is None else self.items[idx]['inventory']
            self.assertEqual(Menu.objects.get(pk=idx).inventory, inventory)
            self.assertEqual(Menu.objects.get(pk=idx).__str__(), f"{self.items[idx]['title']}: ${self.items[idx]['price']:.2f}")
    