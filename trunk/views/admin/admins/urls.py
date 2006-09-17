from django.conf.urls.defaults import *

urlpatterns = patterns('webcon.views.admin.admins.views',
    (r'^$', 'index'),
    (r'^(?P<admin_id>\d+)/$', 'overview'),
    (r'^(?P<admin_id>\d+)/del/$', 'delete'),
    (r'^(?P<admin_id>\d+)/edit/$', 'edit'),
    (r'^(?P<admin_id>\d+)/block/$', 'block'),
    (r'^(?P<admin_id>\d+)/activate/$', 'activate'),
    (r'^new/?$', 'edit'),
    (r'^save/?$', 'save'),
#    (r'^r/', include('django.conf.urls.shortcut')),

)
