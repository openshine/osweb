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
    
    context_dict['project'] = ManageProject.get_project(projectname)
    return render_to_response('projects/project_detail.html', context_dict, context_instance=RequestContext(request))
