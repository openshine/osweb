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


import os

SYSCONF_DIR = os.path.join('@sysconfdir@', '@package@')

#DJANGO DEFINITIONS
#-----------------------------------------------------
DEBUG = True
TEMPLATE_DEBUG = DEBUG

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1

ADMINS = (
    ('Pablo Vieytes', 'pvieytes@openshine.com'),
)
MANAGERS = ADMINS

USE_I18N = True
USE_L10N = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'd1367p85%@qgdx@$aodd5lz6-!m9ku%j*17&%&b&o77a5hh12b'

#APP DEFINITIONS
#-----------------------------------------------------
NEWS_BLOG_URL = "http://blogs.openshine.com/feed/"

MORE_BLOGS_URL = (
    "http://blogs.openshine.com/planet/feed/", 
)


#BLOGS_CACHE_TIME : The timeout, in seconds, to use for the blogs cache
BLOGS_CACHE_TIME = 60*60

#NUM_HOME_NEWS : news number that will be displayed in home page
NUM_HOME_NEWS = 2

#NUM_HOME_PROJECTS : projects number that will be displayes in home page 
NUM_HOME_PROJECTS = 3

#NUM_LIVE_POSTS : post number that will be displayed in live page
NUM_LIVE_POSTS = 8

#NUM_LIVE_RECENT_POSTS : recent post number that will be displayed in live page
NUM_LIVE_RECENT_POSTS = 8

#TWEETS_CACHE_TIME : The timeout, in seconds, to use for the projects cache
TWEETS_CACHE_TIME = 60*60
NUM_TWEETS = 5
TWITTER_USER = "openshine"

#SLIDE_TIMER : Number of miliseconds per slide at home
SLIDE_TIMER = 9000


#PROJECTS_CACHE_TIME : The timeout, in seconds, to use for the projects cache
PROJECTS_CACHE_TIME = 60*60     

NUM_PROJECTS_HOME = 3

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

try:
    LOCAL_CONF = os.path.join(SYSCONF_DIR, 'local.conf')
    if os.path.exists(LOCAL_CONF) :
        execfile(LOCAL_CONF)
except:
    print "Something wrong reading %s" % LOCAL_CONF
    print "  * Check if you have the correct permissions"
    print "  * Check if the configuration is correct"
    
