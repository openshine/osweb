from django.shortcuts import render_to_response
from django.template import RequestContext
from osweb.blogs import ManageBlog


def home_view(request):
    news = ManageBlog.get_home_page_blog()
    context_dict = {}
    context_dict['news'] = news
    return render_to_response('home.html', context_dict, context_instance=RequestContext(request))