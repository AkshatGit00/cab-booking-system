from abc import ABC, abstractmethod
class CabService(ABC):
    @abstractmethod
    def get_id(self):
        pass
    
    @abstractmethod
    def get_cab_number(self):
        pass
    
    @abstractmethod
    def get_driver_name(self):
        pass
    
    @abstractmethod
    def get_location(self):
        pass
    
    @abstractmethod
    def get_availability(self):
        pass
    
    @abstractmethod
    def set_location(self, location):
        pass

    @abstractmethod
    def set_availability(self, availability):
        pass