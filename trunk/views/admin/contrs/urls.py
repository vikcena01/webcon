from django.conf.urls.defaults import *

urlpatterns = patterns('webcon.views.admin.contrs.views',
    (r'^$', 'index'),
    (r'^(?P<contr_id>\d+)/?$', 'overview'),
    (r'^(?P<contr_id>\d+)/del/?$', 'delete'),
    (r'^(?P<contr_id>\d+)/edit/?$', 'edit'),
    (r'^new/?$', 'edit'),
    (r'^save/?$', 'save'),

)
