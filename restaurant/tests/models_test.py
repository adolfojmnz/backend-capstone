from django.test import TestCase

from ..models import Menu
from .mixins import CreateMenuItemsMixin


class MenuTest(CreateMenuItemsMixin, TestCase):

    def setup(self):
        self.create_menu_items()

    def test_created_items(self):
        for idx in self.items.key():
            inventory = 5 if self.items[idx].get('inventory') is None else self.items[idx]['inventory']
            self.assertEqual(Menu.objects.get(id=idx).inventory, inventory)
            self.assertEqual(Menu.objects.get(id=idx), f"{self.items[idx]['title']}: ${self.items[idx]['price']}")
    