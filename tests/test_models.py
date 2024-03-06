from django.test import TestCase
from app.models import CarAd


class CarAdModelTest(TestCase):
    def test_string_representation(self):
        car_ad = CarAd(brand="Seat")
        self.assertEqual(str(car_ad), car_ad.brand)

    def test_app_label(self):
        self.assertEqual(str(CarAd._meta.app_label), "app")
