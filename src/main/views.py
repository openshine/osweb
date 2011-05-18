from django.shortcuts import render_to_response
from django.template import RequestContext
from osweb.blogs import ManageBlog
from osweb.twitter import ManageTwitter
from osweb.projects import ManageProject
from osweb import settings


def home_view(request):
    context_dict = {}
    news = ManageBlog.get_news_blog()
    context_dict['news'] = news[:settings.NUM_HOME_NEWS]
    context_dict['SLIDE_TIMER'] = settings.SLIDE_TIMER
    projects = ManageProject.get_projects()
    context_dict['projects'] = projects[:settings.NUM_HOME_PROJECTS]
    context_dict['tab_home'] = True
    return render_to_response('home.html', context_dict, context_instance=RequestContext(request))




def live_view(request):
    context_dict = {}
    context_dict['tab_live'] = True
    context_dict['num_tweets'] = settings.NUM_TWEETS
    context_dict['twitter_user'] = settings.TWITTER_USER
    
    tweets = ManageTwitter.get_tweets()
    context_dict['tweets'] = tweets
    
    posts = ManageBlog.get_all_blogs()
    context_dict['posts'] = posts
    context_dict['slice_str'] = "0:%s" % settings.NUM_LIVE_POSTS
    print context_dict['slice_str']
    return render_to_response('main/live.html', context_dict, context_instance=RequestContext(request))


def company_view(request):
    context_dict = {}
    projects = ManageProject.get_projects()
    context_dict['projects'] = projects
    context_dict['tab_company'] = True
    return render_to_response('company/company_index.html', context_dict, context_instance=RequestContext(request))




def jobs_view(request):
    context_dict = {}
    return render_to_response('main/jobs.html', context_dict, context_instance=RequestContext(request))


def contact_view(request):
    context_dict = {}
    context_dict['tab_contact'] = True
    return render_to_response('main/contact.html', context_dict, context_instance=RequestContext(request))

#
#
#def projects_view(request):
#    context_dict = {}
#    context_dict['tab_projects'] = True
#    projects = ManageProject.get_projects()
#    context_dict['projects'] = projects
#    context_dict['tab_home'] = True
#    return render_to_response('projects/projects.html', context_dict, context_instance=RequestContext(request))


