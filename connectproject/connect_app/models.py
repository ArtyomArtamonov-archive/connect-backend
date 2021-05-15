from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Tag(models.Model):
    tag = models.CharField(max_length=15)


class Event(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    city = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    longitude = models.FloatField()
    latitude = models.FloatField()
    event_time = models.DateTimeField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    