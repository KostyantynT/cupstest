from django.conf.urls import patterns, url
from cupstest import settings

from contacts import views

urlpatterns = patterns('',
     url(r'^$', views.index, name='index'),
     (r'^static/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}),
)
