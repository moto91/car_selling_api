from rest_framework import serializers
from app.models import CarAd


class CarAdSerializer(serializers.HyperlinkedModelSerializer):
    """
    Hyperlinked serializer automatically generates a set of fields
    based on the model, generates validators for the serializer
    and includes default implementations of .create() and .update().
    It uses hyperlinks to represent relationships, rather than primary keys.
    """
    class Meta:
        model = CarAd
        fields = ['url', 'id', 'created', 'brand', 'model', 'model_year',
                  'description', 'price', 'email']
