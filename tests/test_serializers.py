from django.test import RequestFactory, TestCase
from app.models import CarAd
from app.serializers import CarAdSerializer


class CarAdSerializorTest(TestCase):
    def setUp(self):
        factory = RequestFactory()
        request = factory.get('/')
        self.car_ad_attributes = {'brand': 'Seat',
                                  'model': 'Leon',
                                  'model_year': int(2018),
                                  'price': float(100000),
                                  'email': 'a.m@gmail.com'}
        self.serializer_data = {'brand': 'Seat',
                                'model': 'Leon',
                                'model_year': 2018,
                                'price': 100000,
                                'email': 'a.m@gmail.com'}

        self.car_ad = CarAd.objects.create(**self.car_ad_attributes)
        self.serializer = CarAdSerializer(instance=self.car_ad, context={'request': request})
    def test_contains_expected_fields(self):
        data = self.serializer.data
        assert set(data.keys()) == set(['url', 'id', 'created', 'brand',
                                        'model', 'model_year', 'description', 'price', 'email'])
    def test_blank_email_field(self):
        self.serializer_data['email'] = ''
        serializer = CarAdSerializer(data=self.serializer_data)
        self.assertFalse(serializer.is_valid())
    def test_blank_description_field(self):
        serializer = CarAdSerializer(data=self.serializer_data)
        self.assertTrue(serializer.is_valid())
    def test_price_data_correctly_saves_as_float(self):
        serializer = CarAdSerializer(data=self.serializer_data)
        serializer.is_valid()
        car_ad = serializer.save()
        car_ad.refresh_from_db()
        self.assertIsInstance(car_ad.price, float)
    def test_model_year_data_correctly_saves_as_int(self):
        self.serializer_data['model_year'] = 2018.0
        serializer = CarAdSerializer(data=self.serializer_data)
        serializer.is_valid()
        car_ad = serializer.save()
        car_ad.refresh_from_db()
        self.assertIsInstance(car_ad.model_year, int)
