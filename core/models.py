# core/models.py
from django.db import models
from .exception.exceptions import NoTripAvailableException, TripNotStartedException

class Location(models.Model):
    x = models.FloatField()
    y = models.FloatField()

    def calcDistance(self, locationA, locationB):
        x1, y1 = locationA.x, locationA.y
        x2, y2 = locationB.x, locationB.y
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def __str__(self):
        return f"Location({self.x}, {self.y})"


class Rider(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    rides = models.ManyToManyField('Trip', blank=True, related_name='riders')

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def get_rides(self):
        return self.rides.all()

    def set_location(self, location):
        if not isinstance(location, Location):
            raise ValueError("location must be a Location instance")
        self.location = location
        self.save()

    def __str__(self):
        return f"Rider({self.name})"


class Cab(models.Model):
    cab_number = models.CharField(max_length=20, unique=True)
    driver_name = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)

    def get_id(self):
        return self.id

    def get_cab_number(self):
        return self.cab_number

    def get_driver_name(self):
        return self.driver_name

    def get_location(self):
        return self.location

    def get_availability(self):
        return self.availability

    def set_location(self, location):
        if not isinstance(location, Location):
            raise ValueError("location must be a Location instance")
        self.location = location
        self.save()

    def set_availability(self, availability):
        if not isinstance(availability, bool):
            raise ValueError("availability must be a bool")
        self.availability = availability
        self.save()

    def __str__(self):
        return f"Cab({self.cab_number}, {self.driver_name})"


class Trip(models.Model):
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    cab = models.ForeignKey(Cab, on_delete=models.CASCADE)
    trip_status = models.CharField(
        max_length=20,
        choices=[('IN_PROCESS', 'In Process'), ('ENDED', 'Ended')],
        default='IN_PROCESS'
    )

    def get_rider(self):
        return self.rider

    def get_cab(self):
        return self.cab

    def get_trip_status(self):
        return self.trip_status

    def set_trip_status(self, status):
        if status not in ['IN_PROCESS', 'ENDED']:
            raise ValueError("Invalid trip status")
        self.trip_status = status
        self.save()

    def create_trip(self, rider, cab):
        trip = Trip.objects.create(rider=rider, cab=cab)
        cab.set_availability(False)
        return trip

    def end_trip(self):
        if self.trip_status != 'IN_PROCESS':
            raise TripNotStartedException()
        self.set_trip_status('ENDED')
        self.cab.set_availability(True)

    def __str__(self):
        return f"Trip({self.rider.name} with {self.cab.cab_number})"


# Custom manager for booking-related logic (replaces CabBooking class)
class CabBookingManager(models.Manager):
    def get_available_cabs_for_rider(self, rider):
        if not rider.location:
            raise ValueError("Rider has no location set")

        max_distance = 10.0
        available_cabs = self.filter(availability=True)
        nearest_cab = None
        min_dist = float('inf')

        for cab in available_cabs:
            if cab.location:
                dist = Location().calcDistance(rider.location, cab.location)
                if dist <= max_distance and dist < min_dist:
                    min_dist = dist
                    nearest_cab = cab

        if not nearest_cab:
            raise NoTripAvailableException("No cabs available within range.")

        return nearest_cab


# Attach the custom manager to Cab
Cab.objects = CabBookingManager()