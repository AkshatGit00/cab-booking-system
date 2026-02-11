# core/models.py
from django.db import models
from .exception.exceptions import NoTripAvailableException, TripNotStartedException


class Location(models.Model):
    x = models.FloatField()
    y = models.FloatField()

    @staticmethod
    def calc_distance(location_a, location_b):
        """Calculate Euclidean distance between two locations."""
        x1, y1 = location_a.x, location_a.y
        x2, y2 = location_b.x, location_b.y
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def __str__(self):
        return f"Location({self.x}, {self.y})"


class Rider(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    rides = models.ManyToManyField('Trip', blank=True, related_name='riders')

    @property
    def rider_id(self):
        return self.id

    @property
    def rider_name(self):
        return self.name

    @property
    def rider_location(self):
        return self.location

    @property
    def rider_rides(self):
        return self.rides.all()

    def update_location(self, location):
        """Update rider's location with validation."""
        if not isinstance(location, Location):
            raise ValueError("Location must be a Location instance.")
        self.location = location
        self.save()

    def __str__(self):
        return f"Rider({self.name})"
    

class CabBookingManager(models.Manager):
    def get_nearest_available_cab(self, rider):
        """Find the nearest available cab within max distance."""
        if not rider.location:
            raise ValueError("Rider has no location set.")

        max_distance = 10.0
        available_cabs = self.filter(availability=True)
        nearest_cab = None
        min_dist = float('inf')

        for cab in available_cabs:
            if cab.location:
                dist = Location.calc_distance(rider.location, cab.location)
                if dist <= max_distance and dist < min_dist:
                    min_dist = dist
                    nearest_cab = cab

        if not nearest_cab:
            raise NoTripAvailableException("No cabs available within range.")

        return nearest_cab


class Cab(models.Model):
    cab_number = models.CharField(max_length=20, unique=True)
    driver_name = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)

    objects = CabBookingManager()

    @property
    def cab_id(self):
        return self.id

    @property
    def cab_cab_number(self):
        return self.cab_number

    @property
    def cab_driver_name(self):
        return self.driver_name

    @property
    def cab_location(self):
        return self.location

    @property
    def is_available(self):
        return self.availability

    def update_location(self, location):
        """Update cab's location with validation."""
        if not isinstance(location, Location):
            raise ValueError("Location must be a Location instance.")
        self.location = location
        self.save()

    def update_availability(self, availability):
        """Update cab's availability with validation."""
        if not isinstance(availability, bool):
            raise ValueError("Availability must be a boolean.")
        self.availability = availability
        self.save()

    def __str__(self):
        return f"Cab({self.cab_number}, {self.driver_name})"


class Trip(models.Model):
    IN_PROCESS = 'IN_PROCESS'
    ENDED = 'ENDED'
    TRIP_STATUS_CHOICES = [
        (IN_PROCESS, 'In Process'),
        (ENDED, 'Ended'),
    ]

    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    cab = models.ForeignKey(Cab, on_delete=models.CASCADE)
    trip_status = models.CharField(
        max_length=20,
        choices=TRIP_STATUS_CHOICES,
        default=IN_PROCESS
    )

    @property
    def trip_rider(self):
        return self.rider

    @property
    def trip_cab(self):
        return self.cab

    @property
    def status(self):
        return self.trip_status

    def update_status(self, status):
        """Update trip status with validation."""
        if status not in dict(self.TRIP_STATUS_CHOICES):
            raise ValueError("Invalid trip status.")
        self.trip_status = status
        self.save()

    @classmethod
    def create_trip(cls, rider, cab):
        """Create a new trip and mark cab as unavailable."""
        trip = cls.objects.create(rider=rider, cab=cab)
        cab.update_availability(False)
        return trip

    def end_trip(self):
        """End the trip if in process and make cab available."""
        if self.trip_status != self.IN_PROCESS:
            raise TripNotStartedException()
        self.update_status(self.ENDED)
        self.cab.update_availability(True)

    def __str__(self):
        return f"Trip({self.rider.name} with {self.cab.cab_number})"