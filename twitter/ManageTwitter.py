from osweb import settings
from django.core.cache import cache
import simplejson
import urllib2


class Tweet():
    id = None
    username = None
    url = None
    user_avatar_url = None
    profile_url = None
    html_text = None
    retweeted = None
    retweet_user = None
    date = None

    def set_date(self, date_str):
        self.date = date_str
    
    def set_text(self, plain_text):
        self.html_text = plain_text
        
    def set_profile_url(self):
        pass
    
    def set_tweet_url(self):
        pass  
    
    def set_avatar_url(self):
        pass

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
            tweet.set_avatar_url()
            tweets.append(tweet)    
        
        return tweets
        
        
        
        