from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from banner.models import Course, Section

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # login
    url(r'^login/$', 'django.contrib.auth.views.login'),
    # Redirect
    url(r'^accounts/profile/$', 'banner.views.schedule'),

    # index
    url(r'^$', 'banner.views.index'),
    # courses/<major,minor>_reqs/
    url(r'^courses/major_reqs/$', 'banner.views.courses_major_reqs'),
    url(r'^courses/minor_reqs/$', 'banner.views.courses_minor_reqs'),
    # courses/
    url(r'^courses/$', ListView.as_view(model=Course, template_name='course/lvCourses.html')),
    #url(r'^courses/d+/$', 'banner.views.search_by_course_id'),
    url(r'^courses/(?P<course_id>\d+)$', 'banner.views.search_by_course_id'),
    # sections/
    url(r'^sections/$', ListView.as_view(model=Section, template_name='sections/lvSections_cID.html')),
    url(r'^sections/(?P<pk>\d+)/$', DetailView.as_view(model=Section, template_name='sections/dvSection.html')),
    # Registration and schedule viewing
    url(r'^sections/register/$', 'banner.views.schedule'),
    url(r'^sections/register/(?P<section_id>\d+)$', 'banner.views.register_for_class'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
