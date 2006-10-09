from django.conf.urls.defaults import *

urlpatterns = patterns('webcon.views.user.views',
    (r'^$', 'index'),
    (r'^extra/?$', 'extra'),
    (r'^dwell/?$', 'dwell'),
    (r'^save/?$', 'save'),
#    (r'^r/', include('django.conf.urls.shortcut')),

)
