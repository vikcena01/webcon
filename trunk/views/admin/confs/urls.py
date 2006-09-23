from django.conf.urls.defaults import *

urlpatterns = patterns('webcon.views.admin.confs.views',
    (r'^$', 'index'),
    (r'^(?P<conf_id>\d+)/$', 'overview'),
    (r'^(?P<conf_id>\d+)/del/$', 'delete'),
    (r'^(?P<conf_id>\d+)/edit/$', 'edit'),
    (r'^archive/$', 'archive'),
    (r'^new/$', 'edit'),
    (r'^save/$', 'save'),

    (r'^(?P<conf_id>\d+)/open/$', 'open'),
    (r'^(?P<conf_id>\d+)/close/$', 'close'),

    (r'^archive/(?P<conf_id>\d+)/$', 'overview'),

#    (r'^r/', include('django.conf.urls.shortcut')),

)
