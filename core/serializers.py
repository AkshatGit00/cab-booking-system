from rest_framework import serializers
from .models import Location, Rider, Cab, Trip


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'x', 'y']


class RiderSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)

    class Meta:
        model = Rider
        fields = ['id', 'name', 'location', 'rides']


class CabSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)

    class Meta:
        model = Cab
        fields = ['id', 'cab_number', 'driver_name', 'availability', 'location']


class TripSerializer(serializers.ModelSerializer):
    rider = RiderSerializer(read_only=True)
    cab = CabSerializer(read_only=True)

    class Meta:
        model = Trip
        fields = ['id', 'rider', 'cab', 'trip_status']