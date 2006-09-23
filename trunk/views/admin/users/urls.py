from django.conf.urls.defaults import *

urlpatterns = patterns('webcon.views.admin.users.views',
    (r'^$', 'index'),
    (r'^(?P<user_id>\d+)/?$', 'overview'),
    (r'^(?P<user_id>\d+)/del/?$', 'delete'),
    (r'^(?P<user_id>\d+)/edit/?$', 'edit'),
    (r'^(?P<user_id>\d+)/block/$', 'block'),
    (r'^(?P<user_id>\d+)/activate/$', 'activate'),
    (r'^new/?$', 'edit'),
    (r'^save/?$', 'save'),

)
