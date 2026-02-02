from abstract.CabBookingService import CabBookingService
from abstract.LocationService import LocationService
from Cab import Cab
from exception.exceptions import NoTripAvailableException

class CabBooking(CabBookingService):
    def __init__(self, location_service: LocationService):
        self.__cabs = []
        self.__location_service = location_service

    def get_cabs(self):
        return self.__cabs
    
    def register_cabs(self, cab:Cab):
        if cab in self.__cabs:
            return ValueError("This cab is already registered")
        self.__cabs.append(cab)
        return f"{cab.get_cab_number()} successfully registered."
    
    def get_available_cabs(self, rider):
        max_distance = 10 # uint - km
        for cab in self.__cabs:
            distance = self.__location_service.calcDistance(rider.get_location(), cab.get_location())
            if distance <= max_distance and cab.get_availability():
                return cab
        raise NoTripAvailableException(message="No cabs available.")

