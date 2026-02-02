from django.contrib import admin
from django.urls import path

from core.views import home
from pages.views import page_detail
from timetable.views import timetable_view

urlpatterns = [
    path("timetable/", timetable_view, name="timetable"),
    path("p/<slug:slug>/", page_detail, name="page_detail"),
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("p/<slug:slug>/", page_detail, name="page_detail"),
]
