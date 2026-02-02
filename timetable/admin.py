from django.contrib import admin

from .models import Session


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ("name", "day", "start_time", "end_time", "is_active")
    list_filter = ("day", "is_active")
    search_fields = ("name", "location", "description")
