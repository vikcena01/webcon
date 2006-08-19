from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^webcon/', include('webcon.apps.foo.urls.foo')),
    
    (r'^hotels/', include('webcon.hotels.urls')),
    (r'^m/(.*)$', 'django.views.static.serve', {'document_root': '/home/webcon/_media', 'show_indexes': True}),
    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)
