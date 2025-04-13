from rest_framework import serializers
from .models import *


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            'id', 'lat', 'lon', 'address', 'description', 'region'
        )


class PartnerApplicationObjectSerializer(serializers.ModelSerializer):

    location = LocationSerializer(write_only=True)

    class Meta:
        model = PartnerApplicationObject
        fields = (
            'id', 'type', 'floor', 'area', 'price', 'rent', 'location'
        )

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        location = Location.objects.create(**location_data)
        validated_data['location'] = location

        return super().create(validated_data)