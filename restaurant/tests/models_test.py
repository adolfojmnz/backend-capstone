from django.test import TestCase

from ..models import Menu

class MenuTest(TestCase):
    items = {
        1: {'title': 'Icecream', 'price': 5.00, 'inventory': 7},
        2: {'title': 'IrishCoffe', 'price': 7.89, 'inventory': 13},
        3: {'title': 'Latte', 'price': 3.99, 'inventory': 0},
        4: {'title': 'ApplePie', 'price': 13.78},
    }

    def setup(self):
        for idx in self.items.keys():
            item = Menu.objects.create(
                title = self.items[idx]['title'],
                price = self.items[idx]['price'],
            )
            if self.items[idx].get('inventory'):
                item.inventory = self.items[idx].get('inventory')
            item.save()

    def test_created_items(self):
        for idx in self.items.key():
            inventory = 5 if self.items[idx].get('inventory') is None else self.items[idx]['inventory']
            self.assertEqual(Menu.objects.get(id=idx).inventory, inventory)
            self.assertEqual(Menu.objects.get(id=idx), f"{self.items[idx]['title']}: ${self.items[idx]['price']}")