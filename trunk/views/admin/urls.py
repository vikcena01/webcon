from django.conf.urls.defaults import *

urlpatterns = patterns('webcon.views.admin',
    (r'^confs/', include('views.admin.confs.urls')),
    (r'^hotels/', include('views.admin.hotels.urls')),
    (r'^admins/', include('views.admin.admins.urls')),
    (r'^users/', include('views.admin.users.urls')),
    (r'^contr/', include('views.admin.contrs.urls')),
#    (r'^r/', include('django.conf.urls.shortcut')),

)
