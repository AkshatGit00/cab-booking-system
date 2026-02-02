from abstract.CabService import CabService


class Cab(CabService):

    def __init__(self, id:int, cabNumber:str, driverName:str):
        self.__id = id
        self.__cabNumber = cabNumber
        self.__driverName = driverName
        self.__availability = True
        self.__location = None

    def get_id(self):
        return self.__id
    
    def get_cab_number(self):
        return self.__cabNumber
    
    def get_driver_name(self):
        return self.__driverName
    
    def get_location(self):
        return self.__location
    
    def get_availability(self):
        return self.__availability
    
    def set_location(self, location):
        if not isinstance(location, tuple):
            raise ValueError("location must be a tuple")
        self.__location = location

    def set_availability(self, availability):
        if not isinstance(availability, bool):
            raise ValueError("availability must be a bool field.")
        self.__availability = availability