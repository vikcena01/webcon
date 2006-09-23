from django.conf.urls.defaults import *

urlpatterns = patterns('webcon.views.user.views',
    (r'^$', 'index'),
    (r'^(?P<user_id>\d+)/$', 'overview'),
    (r'^(?P<admin_id>\d+)/del/$', 'delete'),
    (r'^(?P<admin_id>\d+)/edit/$', 'edit'),
    (r'^new/?$', 'edit'),
    (r'^save/?$', 'save'),
#    (r'^r/', include('django.conf.urls.shortcut')),

)
