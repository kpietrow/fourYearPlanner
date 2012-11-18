from banner.models import Course, Section, Major, Minor, Professor, User_Section_Track
from django.http import HttpResponse, Http404
from django.views.generic import ListView


def hello(request):
    """Test"""
    return HttpResponse('Hello World!')
from banner.models import Course, Section, User_Section_Track
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def track_section(request, user_name, section_id):
    """Track section"""
    new_update = User_Section_Track(name=user_name, section=section_id)
    new_update.save()
    return HttpResponse('Your course tracking has been successfully activated.')


def courses_by_major_id(request, major_id):
    """Look up major courses by its ID"""
    try:
        response = HttpResponse(Course.objects.filter(major_id__exact=major_id))
        return response
    except ValueError:
        raise Http404()


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

def schedule(request):
    return render(
        request,
        template_name='sections/schedule.html',
        dictionary={
            'sections': Section.objects.filter(user__exact=request.user),
            'user': request.user
        }
    )


def register_for_class(request, section_id):
    #return HttpResponse([f + '\n' for f in dir(request.user)])
    section = Section.objects.get(pk=section_id)
    if request.user.can_register(section):
        request.user.section_set.add(section)
        request.user.save()
    else:
        return HttpResponse("ERROR")
    return HttpResponseRedirect('/')  # Redirect after POST
