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


from django.shortcuts import render_to_response
from django.template import RequestContext
from osweb.projects import ManageProject


def projects_view(request):
    context_dict = {}
    context_dict['tab_projects'] = True
    projects = ManageProject.get_projects()
    context_dict['projects'] = projects
    return render_to_response('projects/projects.html', context_dict, context_instance=RequestContext(request))



def project_detail(request, projectname):
    context_dict = {}
    context_dict['link'] = "http://www.openshine.com" + request.path
    context_dict['project'] = ManageProject.get_project(projectname)
    return render_to_response('projects/project_detail.html', context_dict, context_instance=RequestContext(request))
