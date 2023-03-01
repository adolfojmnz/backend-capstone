from ..models import Menu

import requests


class CreateMenuItemsMixin:
    items = {
        1: {'title': 'Icecream', 'price': 5.00, 'inventory': 7},
        2: {'title': 'IrishCoffe', 'price': 7.89, 'inventory': 13},
        3: {'title': 'Latte', 'price': 3.99, 'inventory': 0},
        4: {'title': 'ApplePie', 'price': 13.78},
    }

    def create_menu_items(self):
        for idx in self.items.keys():
            item = Menu.objects.create(
                title = self.items[idx]['title'],
                price = self.items[idx]['price'],
            )
            if self.items[idx].get('inventory') is not None:
                item.inventory = self.items[idx].get('inventory')
            item.save()


class UserMixin:

    def create_user(self, username, password):
        url = 'http://127.0.0.1:8000/auth/users/'
        data = {
            'username': username,
            'password': password,
        }
        return requests.post(url, data=data)

    def get_token(self, username, password):
        url = 'http://127.0.0.1:8000/api/token/login/'
        data = {
            'username': username,
            'password': password,
        }
        return requests.post(url, data=data).json().get('access')

    def get_auth_header(self, token):
        return {'Authorization': f'JWT {token}'}
    