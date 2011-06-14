from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'commons.views.home', name='home'),
    # url(r'^commons/', include('commons_core.urls')),
    (r'^$', "commons_core.views.index"),
    (r'^apps/$', 'commons_core.views.appindex'),
    (r'^apps/category/(?P<cat_id>\d+)/$', 'commons_core.views.catdetail'),
    (r'^apps/(?P<app_id>\d+)/$', 'commons_core.views.appdetail'),
    url(r'^apps/(?P<app_id>\d+)/edit/$','commons_core.views.app_edit',name='app_edit'),
    (r'^j/$', 'commons_core.views.j_index'),
    (r'^j/(?P<j_id>\d+)/$', 'commons_core.views.j_detail'),
    url(r'^j/(?P<j_id>\d+)/edit/$','commons_core.views.j_edit',name='jurisdiction_edit'),
    (r'^dep/$', 'commons_core.views.depindex'),
    url(r'^dep/(?P<dep_id>\d+)/$', 'commons_core.views.depdetail',name='deployment_detail'),
    (r'^dep/(?P<dep_id>\d+)/edit/$', 'commons_core.views.depedit'),
    url(r'^dep/add/(?P<app_id>\d+)/$', 'commons_core.views.depedit',name='deployment_add'),
    (r'^admin/', include(admin.site.urls)),
    (r'^users/', include('userena.urls')),
    (r'^messages/', include('userena.contrib.umessages.urls')),
    (r'^invite/', include('privatebeta.urls')),
    #(r'^', include('filer.server.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

