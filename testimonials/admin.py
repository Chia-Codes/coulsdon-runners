from django.contrib import admin

from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("author", "is_featured", "created_at")
    list_filter = ("is_featured",)
    search_fields = ("author", "quote")
