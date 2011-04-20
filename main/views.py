from django.shortcuts import render_to_response
from django.template import RequestContext
from osweb.blogs import ManageBlog
from osweb import settings

def home_view(request):
    news = ManageBlog.get_home_page_blog()
    context_dict = {}
    context_dict['news'] = news
    return render_to_response('home.html', context_dict, context_instance=RequestContext(request))


def live_view(request):
    context_dict = {}
    context_dict['num_tweets'] = settings.NUM_TWEETS
    context_dict['twitter_user'] = settings.TWITTER_USER
    return render_to_response('main/live.html', context_dict, context_instance=RequestContext(request))


