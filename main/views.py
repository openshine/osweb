from django.shortcuts import render_to_response
from django.template import RequestContext
from osweb.blogs import ManageBlog


def home_view(request):
    print ManageBlog.get_corp_blog()
    return render_to_response('home.html', context_instance=RequestContext(request))