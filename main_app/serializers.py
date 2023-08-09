from rest_framework import serializers 
from .models import Hotel

class HotelSerializer(serializers):
    class Meta:
        model = Hotel
        fields = '__all__'
    