from rest_framework import serializers
from .models import *


class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'longitude', 'latitude')


class TagDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
