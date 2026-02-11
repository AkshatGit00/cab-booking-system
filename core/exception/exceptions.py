class NoTripAvailableException(Exception):
    """Exception raised when no cab is available within range."""
    def __init__(self, message="No Cabs available right now. Please try again later!"):
        super().__init__(message)


class TripNotStartedException(Exception):
    """Exception raised when trying to end a non-started trip."""
    def __init__(self, message="Cannot End Trip. Trip not Started Yet."):
        super().__init__(message)