from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from banner.models import Course, Section
from banner.views import Section_Detail_View

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fourYearPlanner.views.home', name='home'),
    # url(r'^fourYearPlanner/', include('fourYearPlanner.foo.urls')),
 git
    url(r'^courses/$', ListView.as_view(model=Course,)),
    url(r'^courses/by_major/\d+/$', 'banner.view.courses_by_major_id'),
    url(r'^courses/by_minor/\d+/$', 'banner.view.courses_by_minor_id'),
    url(r'^courses/Sections_by_semester/\d+/$', 'banner.view.sections_by_semester'),
    url(r'^sections/Section/$', ListView.as_view(model=Section,)),
    url(r'^courses/AllCourses/$', 'banner.view.all_courses'),
    url(r'^sections/register/$', 'banner.views.register'),
    url(r'^sections/track/$', 'banner.views.track_section'),

    # not sure if url is correct here
    url(r'^(?P<slug>[-_\w)+)/$', Section_Detail_View.as_view(), name='article-detail'),


    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)



# ListView, list of objects. while executing, self.object_list will contain list of objects

# DetailView, page representing individual object. while executing, self.object will contain object being
# operated on
