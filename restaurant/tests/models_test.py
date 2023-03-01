from django.test import TestCase

from datetime import datetime

from ..models import Booking, Menu
from .mixins import CreateBookingsMixin, CreateMenuItemsMixin


class MenuTest(CreateMenuItemsMixin, TestCase):

    def setUp(self):
        self.create_menu_items()

    def test_created_items(self):
        for idx in self.items.keys():
            inventory = 5 if self.items[idx].get('inventory') is None else self.items[idx]['inventory']
            self.assertEqual(Menu.objects.get(pk=idx).inventory, inventory)
            self.assertEqual(Menu.objects.get(pk=idx).__str__(), f"{self.items[idx]['title']}: ${self.items[idx]['price']:.2f}")
    
    
class BookingTest(CreateBookingsMixin, TestCase):

    def setUp(self):
        self.create_bookings()
    
    def set_detault_booking_parameters(self, idx):
        if self.bookings[idx].get('no_of_guets') is None:
            self.bookings[idx]['no_of_guests'] = 6
        if self.bookings[idx].get('booking_date') is None:
            self.bookings[idx]['booking_date'] = datetime.today().date()

    def test_created_bookings(self):
        for idx in self.bookings.keys():
            self.set_detault_booking_parameters(idx)
            self.assertEqual(Booking.objects.get(pk=idx).name, self.bookings[idx]['name'])
            self.assertEqual(Booking.objects.get(pk=idx).no_of_guests, self.bookings[idx]['no_of_guests'])
            self.assertEqual(Booking.objects.get(pk=idx).booking_date, self.bookings[idx]['booking_date'])
            