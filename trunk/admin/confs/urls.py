from django.conf.urls.defaults import *

urlpatterns = patterns('webcon.admin.confs.views',
    (r'^$', 'index'),
    (r'^(?P<conf_id>\d+)/?$', 'overview'),
    (r'^(?P<conf_id>\d+)/del/?$', 'delete'),
    (r'^(?P<conf_id>\d+)/edit/?$', 'edit'),
    (r'^new/?$', 'edit'),
    (r'^save/?$', 'save'),
#    (r'^r/', include('django.conf.urls.shortcut')),

)
