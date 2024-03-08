from django.test import RequestFactory, TestCase
from app.models import CarAd
from app.views import CarAdViewSet


class CarAdViewSetTest(TestCase):
    def test_view_get_all(self):
        api_request = RequestFactory().get('/car_ads')
        view = CarAdViewSet.as_view({'get': 'list'})
        response = view(api_request)
        self.assertEqual(response.status_code, 200)

    def test_view_one_ad(self):
        api_request = RequestFactory().get('/car_ads')
        view = CarAdViewSet.as_view({'get': 'list'})
        car_ad = CarAd(brand='Seat', model='Leon', model_year=2018,
                       price=100000, email='a.m@gmail.com')
        car_ad.save()
        response = view(api_request, pk=car_ad.pk)
        self.assertEqual(str(car_ad), response.data['results'][0]['brand'])
        self.assertEqual(response.status_code, 200)

    def test_view_post(self):
        api_request = RequestFactory().post('/car_ads',
                                            data={'brand': 'Seat',
                                                  'model': 'Leon',
                                                  'model_year': 2018,
                                                  'price': 100000,
                                                  'email': 'a.m@gmail.com'})
        view = CarAdViewSet.as_view({'post': 'create'})
        response = view(api_request)
        self.assertEqual(response.status_code, 201)

    def test_view_delete(self):
        car_ad = CarAd(brand='Seat', model='Leon', model_year=2018,
                       price=100000, email='a.m@gmail.com')
        car_ad.save()
        api_request = RequestFactory().delete('/car_ads',
                                              data={'brand': 'Seat',
                                                    'model': 'Leon',
                                                    'model_year': 2018,
                                                    'price': 100000,
                                                    'email': 'a.m@gmail.com'})
        view = CarAdViewSet.as_view({'delete': 'destroy'})
        response = view(api_request, pk=car_ad.pk)
        self.assertEqual(response.status_code, 204)
