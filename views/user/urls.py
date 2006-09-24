from django.conf.urls.defaults import *

urlpatterns = patterns('webcon.views.user.views',
    (r'^$', 'index'),
    (r'^(?P<user_id>\d+)/$', 'index'),
    (r'^(?P<user_id>\d+)/extra/$', 'extra'),
    (r'^new/?$', 'edit'),
    (r'^save/?$', 'save'),
#    (r'^r/', include('django.conf.urls.shortcut')),

)
