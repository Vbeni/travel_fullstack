from django.shortcuts import render
# Importing necessary libraries and modules
from rest_framework import viewsets, permissions
from .models import Hotel, Room, CustomUser, Booking, Review
from .serializers import HotelSerializer, RoomSerializer, CustomUserSerializer, BookingSerializer, ReviewSerializer

# Defining the HotelViewSet
class HotelViewSet(viewsets.ModelViewSet):
    """
    This viewset will provide CRUD (Create, Read, Update, Delete) operations for the Hotel model.
    """
    queryset = Hotel.objects.all()   # Fetching all the Hotel objects from the database
    serializer_class = HotelSerializer  # Using the HotelSerializer to serialize the data

# Defining the RoomViewSet
class RoomViewSet(viewsets.ModelViewSet):
    """
    This viewset will provide CRUD operations for the Room model.
    """
    queryset = Room.objects.all()   # Fetching all the Room objects from the database
    serializer_class = RoomSerializer  # Using the RoomSerializer to serialize the data

# Defining the CustomUserViewSet
class CustomUserViewSet(viewsets.ModelViewSet):
    """
    This viewset will provide CRUD operations for the CustomUser model.
    """
    queryset = CustomUser.objects.all()   # Fetching all the CustomUser objects from the database
    serializer_class = CustomUserSerializer  # Using the CustomUserSerializer to serialize the data
    permission_classes = [permissions.IsAuthenticated]
# Defining the BookingViewSet
class BookingViewSet(viewsets.ModelViewSet):
    """
    This viewset will provide CRUD operations for the Booking model.
    """
    queryset = Booking.objects.all()   # Fetching all the Booking objects from the database
    serializer_class = BookingSerializer  # Using the BookingSerializer to serialize the data

# Defining the ReviewViewSet
class ReviewViewSet(viewsets.ModelViewSet):
    """
    This viewset will provide CRUD operations for the Review model.
    """
    queryset = Review.objects.all()   # Fetching all the Review objects from the database
    serializer_class = ReviewSerializer  # Using the ReviewSerializer to serialize the data
