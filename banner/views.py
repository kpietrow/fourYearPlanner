# Create your views here.
from banner.models import Course, Section, Major, Minor, Professor, User_section_track
from django.http import HttpResponse
from django.views.generic import ListView

def register(request):
    """Register for a class"""
    

    

def track_section(request, section_id):
    """Track section"""
    new_update = User_Section_Track..update(


def courses_by_major_id(request, major_id):
    """Look up major courses by its ID"""
    response = HttpResponse(Course.objects.filter(major_id__exact=major_id))
    return response


def courses_by_minor_id(request, minor_id):
    """Look up minor courses by its ID"""
    response = HttpResponse(Course.objects.filter(minor_id__exact=minor_id))
    return response

def all_courses(request, major_id, minor_id):
    """Look up all courses for major and minor"""
    response = Course.objects.filter(minor_id__exact=minor_id) + Course.objects.filter(major_id__exact=major_id)
    response = set(response)
    response = HttpResponse(response)
    return response

def sections_by_semester(request, semester_id):
    """Look up all sections for semester"""
    response = HttpResponse(Section.objects.filter(semester_id__exact=semester_id))
    return response

