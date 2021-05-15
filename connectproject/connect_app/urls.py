from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('events/create/', EventCreateView.as_view()),
    path('events/all/', EventsListView.as_view()),
    path('events/detail/<int:pk>', EventDetailView.as_view()),
    path('tags/create/', TagCreateView.as_view()),
    path('tags/all/', TagListView.as_view()),
]
