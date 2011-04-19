from django.conf.urls.defaults import *
from osweb import settings


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       
    (r'^$', include('main.urls')),

)


#If not in DJAPP engine add static media folder as static server
if not 'DJAPPS_SERVER' in dir(settings):
    urlpatterns += patterns('',
        (r'^static_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )