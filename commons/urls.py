from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'commons.views.home', name='home'),
    # url(r'^commons/', include('commons.foo.urls')),
    (r'^$', "commons.views.index"),
    (r'^apps/(?P<app_id>\d+)/$', 'commons.views.detail'),
   # (r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
   # (r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
   # (r'^admin/', include(admin.site.urls)),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
