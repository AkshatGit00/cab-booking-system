from abc import ABC, abstractmethod

class CabBookingService:

    @abstractmethod
    def get_cabs(self):
        pass
    
    @abstractmethod
    def register_cabs(self, cab):
        pass
    
    @abstractmethod
    def get_available_cabs(self, rider):
        pass