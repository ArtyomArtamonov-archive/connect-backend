from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

# admin.site.unregister(User)
admin.site.register(Tag)


class EventInline(admin.TabularInline):
    model = Event


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = [EventInline]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'event_time'
    )
