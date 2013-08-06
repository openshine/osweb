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
import os.path

from django.core.exceptions import ImproperlyConfigured

import dj_database_url

def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

PROJECT_DIR = os.path.dirname(__file__)
SYSCONF_DIR = os.path.join('@sysconfdir@', '@package@')

DATABASES = {'default': dj_database_url.config()}

TIME_ZONE = 'Europe/Madrid'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1

SECRET_KEY = get_env_variable("OSWEB_SECRET_KEY")

ADMINS = (
    ('Pablo Vieytes', 'pvieytes@openshine.com'),
)
MANAGERS = ADMINS

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_ROOT = ''
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'osweb.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

INSTALLED_APPS = (
    #'django.contrib.auth',
    #'django.contrib.contenttypes',
    #'django.contrib.sessions',
    #'django.contrib.sites',
    #'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'django.contrib.staticfiles',
    'osweb'
)

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