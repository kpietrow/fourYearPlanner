from django.conf.urls import patterns, include, url
from django.view.generic import ListView
from banner.models import Course
from django.view.generic import SectionDetailView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fourYearPlanner.views.home', name='home'),
    # url(r'^fourYearPlanner/', include('fourYearPlanner.foo.urls')),

    url(r'^courses/$', ListView.as_view(model=Course,)),
    url(r'^courses/by_major/\d+/$', 'banner.view.courses_by_major_id'),
    url(r'^courses/by_minor/\d+/$', 'banner.view.courses_by_minor_id'),
    url(r'^sections/Section/ListView/$', ListView.as_view(model=Section,)),
    url(r'^courses/AllCourses/$', ,
    url(r'^sections/Section/$', DetailView.as_view(), name='section-detail'),
    url(r'^sections/register/$', 'banner.views.register'),                   
    url(r'^sections/track/$', 'banner.views.track'),
    

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)



# ListView, list of objects. while executing, self.object_list will contain list of objects

# DetailView, page representing individual object. while executing, self.object will contain object being
# operated on
