from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room




# Create your views here.
#an endpoint is the thing after slash\

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer