from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'commons.views.home', name='home'),
    # url(r'^commons/', include('commons.foo.urls')),
    (r'^$', "commons_core.views.index"),
    (r'^apps/$', 'commons_core.views.appindex'),
    (r'^apps/(?P<app_id>\d+)/$', 'commons_core.views.detail'),
    url(r'^admin/', include(admin.site.urls)),
)
