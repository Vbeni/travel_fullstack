from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import HotelViewSet, RoomViewSet, CustomUserViewSet, BookingViewSet, ReviewViewSet


router = DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'users', CustomUserViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]