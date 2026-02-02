from abc import ABC, abstractmethod

class TripService:

    @abstractmethod
    def get_rider(self):
        pass
    
    @abstractmethod
    def get_cab(self):
        pass
    
    @abstractmethod
    def get_trip_status(self):
        pass
    
    @abstractmethod
    def set_trip_status(self, status):
        pass

    @abstractmethod
    def create_trip(self, rider, cab):
        pass

    @abstractmethod
    def end_trip(self, cab):
        pass