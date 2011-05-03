from django.conf.urls.defaults import *

from osweb.projects.views import projects_view, project_detail

urlpatterns = patterns('',
    url('^$', projects_view, name='projects_page'),
    url('^(?P<projectname>[-\w]+)/$', project_detail, name='project_detail_page'),

)