from django.conf.urls.defaults import *

from osweb.projects.views import projects_view

urlpatterns = patterns('',
    url('^$', projects_view, name='projects_page'),
  

)