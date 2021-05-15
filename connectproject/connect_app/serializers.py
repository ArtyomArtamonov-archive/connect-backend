from rest_framework import serializers
from .models import *
from .mixins import OrganizerMixin


class TagDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class EventDetailSerializer(serializers.ModelSerializer):
    tags = TagDetailSerializer(many=True)
    organizer = serializers.SerializerMethodField()

    def get_organizer(self, instance):
        return instance.organizer.email
    
    class Meta:
        model = Event
        fields = '__all__'
