from abstract.LocationService import LocationService

class Location(LocationService):

    def calcDistance(self, locationA, locationB):
        x1, y1 = locationA
        x2, y2 = locationB
        return int(((x2-x1)**2 + (y2-y1)**2)**0.5)