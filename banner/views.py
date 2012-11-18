# Create your views here.
from banner.models import Course, Section, Major, Minor, Professor, User_section_track
from django.http import HttpResponse
from django.view.generic import ListView

def register(request):
    """Register for a class"""
    

    

def track(request):
    """Track section"""
    


def courses_by_major_id(request, major_id):
    """Look up major courses by its ID"""
    response = HttpResponse(Course.objects.filter(major_id__exact=major_id))
    return response


def courses_by_minor_id(request, minor_id):
    """Look up minor courses by its ID"""
    response = HttpResponse(Course.objects.filer(minor_id__exact=minor_id))
    return response
