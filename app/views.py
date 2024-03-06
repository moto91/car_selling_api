from app.models import CarAd
from app.serializers import CarAdSerializer
from rest_framework import viewsets, filters


class CarAdViewSet(viewsets.ModelViewSet):
    queryset = CarAd.objects.all()
    serializer_class = CarAdSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created', 'price']
