from django.shortcuts import render
from rest_framework import generics
from .serializers import *


class EventCreateView(generics.CreateAPIView):
    serializer_class = EventDetailSerializer


class TagCreateView(generics.CreateAPIView):
    serializer_class = TagDetailSerializer
