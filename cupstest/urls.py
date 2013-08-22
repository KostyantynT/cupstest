from django.conf.urls import patterns, include, url
from cupstest import settings
from contacts.views import IndexView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='contact_index'),
    url(r'^contacts/', include('contacts.urls')),
    url(r'^middleware/', include('middleware.urls')),
    # Examples:
    # url(r'^$', 'cupstest.views.index', name='index'),
    # url(r'^cupstest/', include('cupstest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^login/$', 'django.contrib.auth.views.login'),
    #url(r'^login/$', 'django.contrib.auth.views.login', {'next': '/'}, name='auth_login'),
    #url(r'^login/(?P<next>.*)/$', 'django.contrib.auth.views.login', name='auth_login_next'),
    
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/contacts/'}, name='auth_logout'),
    url(r'^logout/(?P<next_page>.*)/$', 'django.contrib.auth.views.logout', name='auth_logout_next'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
)
