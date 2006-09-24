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

    (r'^(?P<conf_id>\d+)/events/$', 'events'),
    (r'^(?P<conf_id>\d+)/extras/$', 'extras'),
    (r'^(?P<conf_id>\d+)/entrants/$', 'entrants'),

    (r'^(?P<conf_id>\d+)/events/(?P<event_id>\d+)/$', 'event_edit'),
    (r'^(?P<conf_id>\d+)/events/(?P<event_id>\d+)/del/$', 'event_delete'),
    (r'^(?P<conf_id>\d+)/events/new/$', 'event_edit'),
    (r'^(?P<conf_id>\d+)/events/save/$', 'event_save'),
#    (r'^r/', include('django.conf.urls.shortcut')),

)
