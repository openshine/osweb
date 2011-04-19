from django.conf.urls.defaults import *

from osweb.main.views import home_view


urlpatterns = patterns('',    
    url ('^$', home_view, name='home_page'),
    )