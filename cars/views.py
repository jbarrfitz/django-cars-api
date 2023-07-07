from rest_framework import generics
from .serializers import CarSerializer
from .models import Car


class CarList(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDetail(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


