from django.shortcuts import render_to_response
from django.template import RequestContext

def projects_view(request):
    context_dict = {}
    return render_to_response('projects/projects.html', context_dict, context_instance=RequestContext(request))



