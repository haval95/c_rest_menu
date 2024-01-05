from restaurant.models import Booking


# TestCase class
from django.test import TestCase


class BookingTest(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(name="IceCream", no_guests=80)
        item_str = item.get_item()
        self.assertEqual(item_str, "IceCream : 80")
