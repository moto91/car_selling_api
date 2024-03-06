from rest_framework import serializers
from app.models import CarAd


class CarAdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarAd
        fields = ['url', 'id', 'created', 'brand', 'model', 'model_year', 'description', 'price', 'email']
