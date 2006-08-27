from django.conf.urls.defaults import *

urlpatterns = patterns('webcon.hotels.views',
    (r'^$', 'index'),
    (r'^(?P<hotel_id>\d+)/?$', 'details'),
    (r'^new/?$', 'new'),
#    (r'^r/', include('django.conf.urls.shortcut')),

)
