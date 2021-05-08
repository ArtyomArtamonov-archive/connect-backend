from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('events/create/', EventCreateView.as_view()),
    path('tags/create/', TagCreateView.as_view()),
]
