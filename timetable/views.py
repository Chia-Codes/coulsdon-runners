from django.shortcuts import render

from .models import Session


def timetable_view(request):
    sessions = Session.objects.filter(is_active=True)
    return render(request, "timetable.html", {"sessions": sessions})
