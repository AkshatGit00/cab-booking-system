from abstract.TripService import TripService
from exception.exceptions import TripNotStartedException


class Trip(TripService):

    def __init__(self):
        self.__rider = None
        self.__cab = None
        self.__tripStatus = None

    def get_rider(self):
        return self.__rider
    
    def get_cab(self):
        if not self.__cab:
            return ValueError("No can assign yet")
        return self.__cab
    
    def get_trip_status(self):
        return self.__tripStatus
    
    def set_trip_status(self, status):
        self.__tripStatus = status

    def create_trip(self, rider, cab):
        self.__rider = rider
        self.__cab = cab
        self.__cab.set_availability(False)
        self.set_trip_status("IN_PROCESS")
        return self
    
    def end_trip(self, cab):
        if self.__tripStatus != "IN_PROCESS":
            raise TripNotStartedException()
        self.set_trip_status("Ended")
        cab.set_availability(True)
        return "Trip ended successfully."