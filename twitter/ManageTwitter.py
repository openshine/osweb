from osweb import settings
from django.core.cache import cache
import simplejson
import urllib2
import re
import time


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
        self.date = time.strptime(date_str, "%a %b %d %H:%M:%S +0000 %Y")#Tue Apr 26 08:57:55 +0000 2011
        print self.date
        
        
        
    
    def set_text(self, plain_text):
        
        http_regex = re.compile(r"(http://[^ ]+)")
        self.html_text = http_regex.sub(r'<a href="\1">\1</a>', plain_text)
                
        https_regex = re.compile(r"(https://[^ ]+)")
        self.html_text = https_regex.sub(r'<a href="\1">\1</a>', self.html_text)
        
        hash_regex = re.compile(r'#[0-9a-zA-Z+_]*',re.IGNORECASE)
        user_regex = re.compile(r'@[0-9a-zA-Z+_]*',re.IGNORECASE)        

        for tt in user_regex.finditer(self.html_text):
            url_tweet = tt.group(0).replace('@','')
            self.html_text = self.html_text.replace(tt.group(0),
                    '<a href="http://twitter.com/'+
                    url_tweet+'" title="'+
                    tt.group(0)+'">'+
                    tt.group(0)+'</a>')
 
        for th in hash_regex.finditer(self.html_text):
                url_hash = th.group(0).replace('#','%23')
                if len ( th.group(0) ) > 2:
                    self.html_text = self.html_text.replace(th.group(0),
                            '<a href="http://search.twitter.com/search?q='+
                            url_hash+'" title="'+
                            th.group(0)+'">'+
                            th.group(0)+'</a>');
                            
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
            ManageTwitter.update_tweets_cahce()
        return cache.get('tweets')
    
    @staticmethod
    def update_tweets_cahce():
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
        
        
        
        