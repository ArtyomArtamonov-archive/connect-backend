from rest_framework import serializers
from .models import *
from .mixins import OrganizerFieldMixin


class TagDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class EventDetailSerializer(OrganizerFieldMixin, serializers.ModelSerializer):
    tags = TagDetailSerializer(many=True)
    
    class Meta:
        model = Event
        fields = '__all__'
