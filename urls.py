from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^webcon/', include('webcon.apps.foo.urls.foo')),
    
    (r'^m/(.*)$', 'django.views.static.serve', {'document_root': '/home/webcon/_media', 'show_indexes': True}),
    
    (r'^hotels/', include('webcon.hotels.urls')),
    (r'^admins/', include('webcon.admins.urls')),
    (r'^users/', include('webcon.users.urls')),
    (r'^confs/', include('webcon.confs.urls')),
    (r'^contr/', include('webcon.contr.urls')),

    (r'^login/?$', 'webcon.auth.views.login'),
    (r'^logout/?$', 'webcon.auth.views.logout'),
    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)
