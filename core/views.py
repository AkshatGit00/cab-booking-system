from rest_framework import generics, status
from rest_framework.response import Response
from .models import Rider, Cab, Trip
from .serializers import RiderSerializer, CabSerializer, TripSerializer
from .exception.exceptions import NoTripAvailableException, TripNotStartedException

class RiderListCreate(generics.ListCreateAPIView):
    queryset = Rider.objects.all()
    serializer_class = RiderSerializer

class CabListCreate(generics.ListCreateAPIView):
    queryset = Cab.objects.all()
    serializer_class = CabSerializer

class TripList(generics.ListAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class BookRideView(generics.CreateAPIView):
    def post(self, request):
        rider_id = request.data.get('rider_id')
        try:
            rider = Rider.objects.get(id=rider_id)
            cab = Cab.objects.get_available_cabs(rider)  # Uses custom manager
            trip = Trip().create_trip(rider, cab)
            serializer = TripSerializer(trip)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Rider.DoesNotExist:
            return Response({'error': 'Rider not found'}, status=status.HTTP_404_NOT_FOUND)
        except NoTripAvailableException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class EndTripView(generics.UpdateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def put(self, request, *args, **kwargs):
        trip = self.get_object()
        try:
            trip.end_trip(trip.cab)
            return Response({'message': 'Trip ended successfully'}, status=status.HTTP_200_OK)
        except TripNotStartedException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)