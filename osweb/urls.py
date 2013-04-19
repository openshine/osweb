#osweb. Main Openshines website 
#Copyright (C) 2011  Openshine sl
# Authors:
#    Pablo Vieytes <pvieytes@openshine.com>
#    Roberto Majadas <roberto.majadas@openshine.com>
#    Cesar Garcia Tapia <cesar.garcia.tapia@openshine.com>
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.


from django.conf.urls.defaults import *
from osweb import settings

from osweb.main.views import home_view
from osweb.main.views import live_view
from osweb.main.views import company_view
from osweb.main.views import jobs_view
from osweb.main.views import contact_view

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',          
    url(r'^$', home_view, name='home_page'),
    url(r'^live/', live_view, name='live_page'),
    url(r'^company/', company_view, name='company_page'),   
    
     
    url(r'^jobs/', jobs_view, name='jobs_page'),
    url(r'^contact/', contact_view, name='contact_page'),
    (r'^projects/', include('osweb.projects.urls')),

)


#If not in DJAPP engine add static media folder as static server
if not 'DJAPPS_SERVER' in dir(settings):
    urlpatterns += patterns('',
                            (r'^m/(?P<path>.*)$', 
                             'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 
                                                           'show_indexes': True}),
                            )
    
    import os
    from django import __file__ as dj_mod_path

    django_path = os.path.dirname(dj_mod_path)
    django_admin_path = os.path.join(django_path, 
                                     'contrib', 
                                     'admin', 
                                     'media') + os.sep
    urlpatterns += patterns('',
                            (r'^sm/admin_media/(?P<path>.*)$', 
                             'django.views.static.serve', {'document_root': django_admin_path, 
                                                           'show_indexes': True}),
                            )
    
    
