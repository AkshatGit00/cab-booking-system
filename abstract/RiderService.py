from abc import ABC, abstractmethod

class RiderService:

    @abstractmethod
    def get_id(self):
        pass
    
    @abstractmethod
    def get_name(self):
        pass
    
    @abstractmethod
    def get_location(self):
        pass
    
    @abstractmethod
    def get_rides(self):
        pass
    
    @abstractmethod
    def set_location(self, location):
        pass