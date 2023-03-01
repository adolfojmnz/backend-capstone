from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from restaurant.models import Menu, Booking
from .serializers import BookingSerializer, MenuSerializer


class MenuItemView(ListCreateAPIView):
    model = Menu
    queryset = model.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    model = Menu
    queryset = model.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class BookingView(ListCreateAPIView):
    model = Booking
    queryset = model.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


class SingleBookingView(RetrieveUpdateDestroyAPIView):
    model = Booking
    queryset = model.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]