from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'commons.views.home', name='home'),
    # url(r'^commons/', include('commons.foo.urls')),
    (r'^$', "commons_core.views.index"),
    url(r'^admin/', include(admin.site.urls)),
)
