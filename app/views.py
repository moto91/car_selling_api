from app.models import CarAd
from app.serializers import CarAdSerializer
from rest_framework import viewsets, filters


class CarAdViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.

    Additionally also provided an extra ordering filter.
    """
    queryset = CarAd.objects.all()
    serializer_class = CarAdSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created', 'price']
