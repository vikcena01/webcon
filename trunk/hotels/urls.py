from django.conf.urls.defaults import *

urlpatterns = patterns('webcon.hotels.views',
    (r'^$', 'index'),
    (r'^(?P<hotel_id>\d+)/?$', 'overview'),
    (r'^(?P<hotel_id>\d+)/del/?$', 'delete'),
    (r'^(?P<hotel_id>\d+)/edit/?$', 'edit'),
    (r'^new/?$', 'edit'),
    (r'^save/?$', 'save'),
#    (r'^r/', include('django.conf.urls.shortcut')),

)
