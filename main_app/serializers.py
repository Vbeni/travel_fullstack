from rest_framework import viewsets
from rest_framework import serializers 
from .models import Hotel, Room, Review, CustomUser, Booking

class HotelSerializer(serializers):
    class Meta:
        model = Hotel
        fields = '__all__'

class RoomSerializer(serializers):
    class Meta:
        model = Room
        fields = '__all__'

class ReviewSerializer(serializers):
    class Meta:
        model = Review
        fields = '__all__'

class BookingSerializer(serializers):
    class Meta:
        model = Booking
        fields = '__all__'

class CustomUserSerializer(serializers):
    class Meta:
        model = CustomUser
        fields = '__all__'



