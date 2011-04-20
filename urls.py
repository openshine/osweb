from django.conf.urls.defaults import *
from osweb import settings

from osweb.main.views import home_view
from osweb.main.views import live_view

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       
    url('^$', home_view, name='home_page'),
    url ('^live/', live_view, name='live_page'),
)


#If not in DJAPP engine add static media folder as static server
if not 'DJAPPS_SERVER' in dir(settings):
    urlpatterns += patterns('',
        (r'^static_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )