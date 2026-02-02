from abstract.CabBookingService import CabBookingService
from abstract.RiderService import RiderService
from abstract.TripService import TripService
from exception.exceptions import NoTripAvailableException


class Rider(RiderService):

    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__location = None
        self.__rides = []

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_location(self):
        return self.__location
    
    def get_rides(self):
        return self.__rides
    
    def set_location(self, location):
        if not isinstance(location, tuple):
            return ValueError("location must be a tuple value.")
        self.__location = location

    def book_ride(self, cab_booking_service:CabBookingService, trip_service:TripService):
        try:
            cab = cab_booking_service.get_available_cabs(self)
        except NoTripAvailableException as e:
            return str(e)
        trip = trip_service.create_trip(self, cab)
        self.__rides.append(trip)
        return trip
