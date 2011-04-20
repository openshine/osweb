from django.conf.urls.defaults import *
from osweb import settings

from osweb.main.views import home_view
from osweb.main.views import live_view
from osweb.main.views import jobs_view
from osweb.main.views import contact_view

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',          
    url(r'^$', home_view, name='home_page'),
    url(r'^live/', live_view, name='live_page'),
    url(r'^jobs/', jobs_view, name='jobs_page'),
    url(r'^contact/', contact_view, name='contact_page'),
    (r'^projects/', include('osweb.projects.urls')),

)


#If not in DJAPP engine add static media folder as static server
if not 'DJAPPS_SERVER' in dir(settings):
    urlpatterns += patterns('',
        (r'^static_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )