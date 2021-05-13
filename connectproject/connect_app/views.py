from rest_framework import generics
from rest_framework import filters
from .serializers import *


class EventCreateView(generics.CreateAPIView):
    serializer_class = EventDetailSerializer


class EventsListView(generics.ListAPIView):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventDetailSerializer
    queryset = Event.objects.all()


class TagCreateView(generics.CreateAPIView):
    serializer_class = TagDetailSerializer

