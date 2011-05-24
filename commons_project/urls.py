from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'commons.views.home', name='home'),
    # url(r'^commons/', include('commons_core.urls')),
    (r'^$', "commons_core.views.index"),
    (r'^apps/(?P<app_id>\d+)/$', 'commons_core.views.detail'),
    (r'^j/(?P<j_id>\d+)/$', 'commons_core.views.j_detail'),
    url(r'^admin/', include(admin.site.urls)),
)
