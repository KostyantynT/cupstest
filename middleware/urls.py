from django.conf.urls import patterns, url
from cupstest import settings
from middleware import views

urlpatterns = patterns('',
     url(r'^$', views.list, name='list'),
     (r'^static/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}),
)