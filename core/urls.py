from django.urls import path
from .views import RiderListCreate, CabListCreate, TripList, BookRideView, EndTripView

urlpatterns = [
    path('riders/', RiderListCreate.as_view(), name='riders'),
    path('cabs/', CabListCreate.as_view(), name='cabs'),
    path('trips/', TripList.as_view(), name='trips'),
    path('book-ride/', BookRideView.as_view(), name='book-ride'),
    path('end-trip/<int:pk>/', EndTripView.as_view(), name='end-trip'),
]