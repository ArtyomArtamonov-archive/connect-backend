from rest_framework import serializers

class OrganizerFieldMixin(serializers.Serializer):
    organizer = serializers.SerializerMethodField()

    def get_organizer(self, instance):
        return instance.organizer.email
