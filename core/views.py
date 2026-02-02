from django.shortcuts import render

from testimonials.models import Testimonial
from timetable.models import Session


def home(request):
    sessions = Session.objects.filter(is_active=True)[:6]
    testimonials = Testimonial.objects.filter(is_featured=True)[:3]
    context = {"sessions": sessions, "testimonials": testimonials}
    return render(request, "home.html", context)
