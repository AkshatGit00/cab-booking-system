from abc import ABC, abstractmethod

class LocationService(ABC):
    @abstractmethod
    def calcDistance(self, locationA, locationB):
        pass