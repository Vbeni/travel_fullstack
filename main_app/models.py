from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.name
    
class Room(models.Model):
    #links each room to a hotel 
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.room_type - self.hotel.name}"
    
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_lenght=15, blank=True, null=True)

    def __str__(self):
        return self.username
    
class Booking(models.MOdel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    status = models.CharField(max_length=10, choices=[('CONFIRMED', 'Confirmed'), ('CANCELLED', 'Canceled')])

    def __str__(self):
        return f"{self.user.username} - {self.room.hotel.name} - {self.check_in_date} to {self.check_out_date}"
