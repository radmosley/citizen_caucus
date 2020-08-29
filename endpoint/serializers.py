from rest_framework import serializers
from endpoint.models import Model

class ModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Model
        fields = [
            'id',
            'first_name',
            'last_name'
        ]