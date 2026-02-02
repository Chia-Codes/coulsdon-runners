from django.contrib import admin

from .models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "published")
    list_filter = ("published",)
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
