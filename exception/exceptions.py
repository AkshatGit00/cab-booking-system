class NoTripAvailableException(Exception):
    def __init__(self, *args, message=None):
        # message = "No Cabs available right now. Please try again later!"
        super().__init__(message)

class TripNotStartedException(Exception):
    def __init__(self, *args):
        message = "Cannot End Trip. Trip not Started Yet."
        super().__init__(message)