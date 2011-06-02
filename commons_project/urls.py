from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'commons.views.home', name='home'),
    # url(r'^commons/', include('commons_core.urls')),
    (r'^$', "commons_core.views.index"),
    (r'^apps/$', 'commons_core.views.appindex'),
    (r'^apps/(?P<app_id>\d+)/$', 'commons_core.views.detail'),
    (r'^j/$', 'commons_core.views.j_index'),
    (r'^j/(?P<j_id>\d+)/$', 'commons_core.views.j_detail'),
    (r'^dep/$', 'commons_core.views.depindex'),
    (r'^dep/(?P<dep_id>\d+)/$', 'commons_core.views.depdetail'),
    (r'^admin/', include(admin.site.urls)),
    (r'^users/', include('userena.urls')),
    (r'^messages/', include('userena.contrib.umessages.urls')),
    #(r'^', include('filer.server.urls')),
)

