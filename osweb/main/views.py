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

import random

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

from osweb.blogs import ManageBlog
from osweb.projects import ManageProject

def home_view(request):
    context_dict = {}
    news = ManageBlog.get_news_blog()
    try :
        context_dict['news'] = news[:settings.NUM_HOME_NEWS]
    except:
        pass
    context_dict['SLIDE_TIMER'] = settings.SLIDE_TIMER
    projects = ManageProject.get_frontpage_projects()
    random.shuffle(projects)
    context_dict['projects'] = projects[:settings.NUM_HOME_PROJECTS]
    context_dict['tab_home'] = True
    return render_to_response('home.html', context_dict, context_instance=RequestContext(request))

def company_view(request):
    context_dict = {}
    projects = ManageProject.get_projects()
    context_dict['projects'] = projects
    context_dict['tab_company'] = True
    return render_to_response('main/company.html', context_dict, context_instance=RequestContext(request))

def jobs_view(request):
    context_dict = {}
    return render_to_response('main/jobs.html', context_dict, context_instance=RequestContext(request))

def contact_view(request):
    context_dict = {}
    context_dict['tab_contact'] = True
    return render_to_response('main/contact.html', context_dict, context_instance=RequestContext(request))


