from rest_framework_gis import serializers

from .models import Toilet

class ToiletSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = Toilet
        geo_field = 'location'
        id_field = 'id'
        fields = ('id', 'type', 'running_water', 'well_lit', 'rating', 'comments', 'location', 'timestamp')

