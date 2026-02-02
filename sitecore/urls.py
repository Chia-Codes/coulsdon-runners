from django.contrib import admin
from django.urls import path

from core.views import home
from pages.views import page_detail

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("p/<slug:slug>/", page_detail, name="page_detail"),
]
