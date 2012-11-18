from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fourYearPlanner.views.home', name='home'),
    # url(r'^fourYearPlanner/', include('fourYearPlanner.foo.urls')),

    url(r'^/$', 'banner.views.index'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


# ListView, list of objects. while executing, self.object_list will contain list of objects

# DetailView, page representing individual object. while executing, self.object will contain object being
# operated on
