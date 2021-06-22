from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django_filters import rest_framework
from .serializers import *
from .filters import *


class EventCreateView(generics.CreateAPIView):
    serializer_class = EventDetailSerializer
    permission_classes = [IsAdminUser]


class EventsListView(generics.ListAPIView):
    search_fields = ['name']
    filter_backends = (rest_framework.DjangoFilterBackend,OrderingFilter)
    filterset_class = EventFilter
    ordering_fields = ['event_time']
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventDetailSerializer
    queryset = Event.objects.all()


class TagCreateView(generics.CreateAPIView):
    serializer_class = TagDetailSerializer


class TagListView(generics.ListAPIView):
    serializer_class = TagDetailSerializer
    queryset = Tag.objects.all()
