from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^webcon/', include('webcon.apps.foo.urls.foo')),
    
    (r'^m/(.*)$', 'django.views.static.serve', {'document_root': '/home/webcon/media', 'show_indexes': True}),
    
    (r'^admin/', include('webcon.views.admin.urls')),
    (r'^user/', include('webcon.views.user.urls')),
    
#    (r'^admin/hotels/', include('webcon.admin.hotels.urls')),
#    (r'^admin/admins/', include('webcon.admin.admins.urls')),
#    (r'^admin/users/', include('webcon.admin.users.urls')),
#    (r'^admin/confs/', include('webcon.views.admin.confs.urls')),
#    (r'^admin/contr/', include('webcon.admin.contr.urls')),

    (r'^login/?$', 'webcon.views.auth.views.login'),
    (r'^logout/?$', 'webcon.views.auth.views.logout'),

    # (r'^$', 'django.views.generic.simple.redirect_to', {''}),
# Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)
