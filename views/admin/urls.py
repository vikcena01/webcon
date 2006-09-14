from django.conf.urls.defaults import *

urlpatterns = patterns('webcon.views.admin',
    (r'^hotels/', include('hotels.urls')),
    (r'^admins/', include('admins.urls')),
    (r'^users/', include('users.urls')),
    (r'^confs/', include('views.admin.confs.u_confs')),
    (r'^contr/', include('contr.urls')),
#    (r'^r/', include('django.conf.urls.shortcut')),

)
