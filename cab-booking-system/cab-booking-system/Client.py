from Cab import Cab
from Rider import Rider
from Location import Location
from CabBooking import CabBooking
from Trip import Trip
from exception.exceptions import NoTripAvailableException, TripNotStartedException

def main():
    try:

        location_service = Location()
        cab_booking_service = CabBooking(location_service)
        trip_service = Trip()

        rider1 = Rider(1, "Akshat")
        rider1.set_location((0, 4))
        rider2 = Rider(2, "Aryan")
        rider2.set_location((0, 7))

        cab1 = Cab(1, "KA086789", "Akash")
        cab1.set_location((9, 8))
        cab2 = Cab(2, "MP074567", "Sunny")
        cab2.set_location((5, 6))

        print("riders", rider1, rider2)
        print("cabs", cab1, cab2)

        print(cab_booking_service.register_cabs(cab1))
        print(cab_booking_service.register_cabs(cab2))

        trip1 = rider1.book_ride(cab_booking_service, trip_service)
        print("trip1", trip1)
        trip2 = rider2.book_ride(cab_booking_service, trip_service)
        print("trip2", trip2)
        trip3 = rider1.book_ride(cab_booking_service, trip_service)
        print("trip3", trip3)
        trip1.end_trip(cab1)
        trip4 = rider1.book_ride(cab_booking_service, trip_service)
        print("trip4", trip4)
    except NoTripAvailableException as e:
        print(str(e))
    except ValueError as e:
        print(str(e))
    except TripNotStartedException as e:
        print(str(e))

if __name__ == "__main__":
    main()