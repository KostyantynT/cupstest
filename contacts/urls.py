from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from cupstest import settings

from contacts import views

urlpatterns = patterns('',
     url(r'^$', views.IndexView.as_view(), name='index'),
     url(r'^(?P<pk>\d+)/$', views.IndexView.as_view(), name='index'),
     url(r'^edit/(?P<pk>\d+)/$', login_required(views.UpdateContactView.as_view()), name='edit'),
     (r'^static/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}),
)
