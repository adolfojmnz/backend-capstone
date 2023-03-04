from django.test import Client, TestCase
from django.urls import reverse

from api.serializers import MenuSerializer, BookingSerializer
from restaurant.models import Menu, Booking
from config.tests.mixins import UserMixin, MenuItemMixin, SingleMenuItemMixin, BookingMixin


class SetUpMixin:

    def setUp(self):
        self.user = self.create_user(                                   
            username = 'test@email.com',                                                                   
            password = 'testpasswd',                 
        )                                                                             
        self.token = self.get_token(
            username = 'test@email.com',                                                                   
            password = 'testpasswd',                 
        )
        self.client = Client(HTTP_AUTHORIZATION=f'JWT {self.token}')


class BookingTest(SetUpMixin, UserMixin, BookingMixin, TestCase):

    def setUp(self):
        self.create_bookings()
        return super().setUp()

    def test_get(self):
        response = self.client.get(reverse('api:bookings')) 
        serializer = BookingSerializer(Booking.objects.all(), many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)


class MenuItemViewTest(SetUpMixin, UserMixin, MenuItemMixin, TestCase):

    def setUp(self):
        self.create_menu_items()
        super().setUp()

    def test_list(self):
        response = self.client.get(reverse('api:menu'))
        serializer = MenuSerializer(Menu.objects.all(), many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_create(self):
        data = {'title': 'latte', 'price': 2.99, 'inventory': 5}
        response = self.client.post(reverse('api:menu'), data=data)
        serializer = MenuSerializer(Menu.objects.get(title='latte'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, serializer.data)
