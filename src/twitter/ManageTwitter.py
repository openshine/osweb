from osweb import settings
from django.core.cache import cache
import simplejson
import urllib2
import re
import time
from time import mktime
from datetime import datetime



class Tweet():
    id = None
    username = None
    url = None
    user_avatar_url = None
    tweet_url = None
    profile_url = None
    html_text = None
    retweeted = None
    retweet_user = None
    date = None

    def set_date(self, date_str):
        time_struct = time.strptime(date_str, "%a %b %d %H:%M:%S +0000 %Y")#Tue Apr 26 08:57:55 +0000 2011
        self.date = datetime.fromtimestamp(mktime(time_struct))
        
    
    def set_text(self, plain_text):
        
        re_http = re.compile(r"(http://[^ ]+)")
        self.html_text = re_http.sub(r'<a href="\1">\1</a>', plain_text)
                
        re_https = re.compile(r"(https://[^ ]+)")
        self.html_text = re_https.sub(r'<a href="\1">\1</a>', self.html_text)
        
        
        re_user = re.compile(r'@[0-9a-zA-Z+_]*',re.IGNORECASE)        
        for iterator in re_user.finditer(self.html_text):
            a_username = iterator.group(0)
            username = a_username.replace('@','')
            link = '<a href="http://twitter.com/' + username + '">' + a_username + '</a>'
            self.html_text = self.html_text.replace(a_username, link)
                    
 
        re_hash = re.compile(r'#[0-9a-zA-Z+_]*',re.IGNORECASE)
        for iterator in re_hash.finditer(self.html_text):
            h_tag = iterator.group(0)
            link_tag = h_tag.replace('#','%23')
            link = '<a href="http://search.twitter.com/search?q=' + link_tag + '">' + h_tag + '</a>'
            self.html_text = self.html_text.replace(h_tag + " ", link + " ")
            #check last tag
            offset = len(self.html_text) - len(h_tag)
            index = self.html_text.find(h_tag, offset)
            if index >= 0:
                self.html_text = self.html_text[:index] + " " + link
            
            
            
                            
                            
    def set_profile_url(self):
        if self.retweeted:
            self.profile_url = "http://www.twitter.com/%s" % self.retweet_user
        else:
            self.profile_url = "http://www.twitter.com/%s" % self.username
    
    def set_tweet_url(self):
        self.tweet_url = "http://www.twitter.com/%s/status/%s" % (self.username, self.id)
    


class ManageTwitter():
    
    @staticmethod
    def get_tweets():
        if cache.get('tweets') is None:
            ManageTwitter.update_tweets_cache()
        return cache.get('tweets')
    
    @staticmethod
    def update_tweets_cache():
        tweets = ManageTwitter.read_tweets()
        cache.set('tweets', tweets, settings.TWEETS_CACHE_TIME)

    
    @staticmethod    
    def read_tweets():
        tweets = []
        url = "http://api.twitter.com/1/statuses/user_timeline.json?screen_name=%s&count=%s&include_rts=true" % (settings.TWITTER_USER, settings.NUM_TWEETS)
        file = urllib2.urlopen(url)        
        content = file.read()        
        json = simplejson.loads(content)
        
        
        for js_tweet in json:
            tweet = Tweet()
            tweet.id = js_tweet['id']
            tweet.username = js_tweet['user']['screen_name']
            try:
                tweet.retweet_user = js_tweet['retweeted_status']['user']['screen_name']
                tweet.retweeted = True
            except:
                tweet.retweeted = False   
            
            tweet.set_date(js_tweet['created_at'])
            tweet.set_tweet_url()#tweet.id, tweet.username must exist
            tweet.set_text(js_tweet['text'])#convert plain text to he
            tweet.set_profile_url()#tweet.id, tweet.username must exist
            if tweet.retweeted:
                tweet.user_avatar_url = js_tweet['retweeted_status']['user']['profile_image_url']
            else:
                tweet.user_avatar_url = js_tweet['user']['profile_image_url']
            tweets.append(tweet)    
        
        return tweets
        
        
        
        