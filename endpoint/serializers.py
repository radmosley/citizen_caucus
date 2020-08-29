from rest_framework import serializers
from endpoint.models import Senator

class SenatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Senator
        fields = [
            'id',
            'first_name',
            'last_name'
        ]