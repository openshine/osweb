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
from osweb.blogs import ManageBlog
from osweb.twitter import ManageTwitter
from osweb.projects import ManageProject
from osweb import settings

import random

def home_view(request):
    context_dict = {}
    news = ManageBlog.get_news_blog()
    context_dict['news'] = news[:settings.NUM_HOME_NEWS]
    context_dict['SLIDE_TIMER'] = settings.SLIDE_TIMER
    projects = ManageProject.get_frontpage_projects()
    random.shuffle(projects)
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
    context_dict['slice_num_post'] = "0:%s" % settings.NUM_LIVE_POSTS
    context_dict['slice_recent_post'] = "0:%s" % settings.NUM_LIVE_RECENT_POSTS
    #context_dict['slice_characters_per_post'] = "0:%s" % 500
    return render_to_response('main/live.html', context_dict, context_instance=RequestContext(request))


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

#
#
#def projects_view(request):
#    context_dict = {}
#    context_dict['tab_projects'] = True
#    projects = ManageProject.get_projects()
#    context_dict['projects'] = projects
#    context_dict['tab_home'] = True
#    return render_to_response('projects/projects.html', context_dict, context_instance=RequestContext(request))


