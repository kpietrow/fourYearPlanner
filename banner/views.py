from banner.models import Course, Section, User_Section_Track, Major, Minor
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render


def index(request):
    return render(request, template_name='index.html')

def track_section(request, user_name, section_id):
    """Track section"""
    new_update = User_Section_Track(name=user_name, section=section_id)
    new_update.save()
    return HttpResponse('Your course tracking has been successfully activated.')


def courses_major_reqs(request):
    """Look up major courses"""
    try:
        courses_by_major = []
        for major in Major.objects.all():
            courses = []
            for course in Course.objects.filter(major_id__exact = major.pk):
                course.prereq = [x.course.name for x in course.major_requirement_set.all()]
            courses.append(course)
        courses_by_major.append(courses)

        return render(
            request,
            template_name='course/degree_reqs.html',
            dictionary={
                'degree': courses_by_major,
                'location': 'course/degree_reqs.html'
            }
        )
    except ValueError:
        raise Http404()


def courses_minor_reqs(request):
    """Look up minor courses by its ID"""
    try:
        courses_by_minor = []
        courses = []
        for minor in Minor.objects.all():
            courses = []
            for course in Course.objects.filter(minor_id__exact = minor.pk):
                course.prereq = [x.course.name for x in course.minor_requirement_set.all()]
            courses.append(course)
        courses_by_minor.append(courses)
        return render(
            request,
            template_name='course/degree_reqs.html',
            dictionary={
                'degree': courses_by_minor,
                'location': 'course/degree_reqs.html'
            }
        )
    except ValueError:
        raise Http404()

def search_by_course_id(request, course_id):
    sections = Section.objects.filter(course_id__exact=course_id)
    return render(
        request,
        template_name='sections/lvSections_cID.html',
        dictionary={
            'sections': sections,
            'location': 'lvSections_cID.html'
        }
    )

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
