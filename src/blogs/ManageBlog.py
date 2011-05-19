from django.core.cache import cache
from osweb import settings
import time
import feedparser
from time import mktime
from datetime import datetime

class Post():
    date = None
    title = None
    link = None
    content = None
    author = None
    blog_url = None
    
    
    def set_content(self, content, cut_out=True):
        """Add only two html paragraph (<p>) to content
        """
        sub_str = '</p>'
        index = content.find(sub_str)
        index = content.find(sub_str, index+len(sub_str))
        if index > -1:
            self.content = content[:index+len(sub_str)]
        else:
            index = content.find(sub_str)
            if index > -1:
                self.content = content[:index+len(sub_str)]
            else:
                self.content = content[:500]

class ManageBlog():
    
    @staticmethod
    def get_news_blog():
        if cache.get('news_blog') is None:
            ManageBlog.update_news_blog()
        return cache.get('news_blog')
        
    @staticmethod    
    def get_all_blogs():
        if cache.get('all_blogs') is None:
            ManageBlog.update_all_blogs()
        return cache.get('all_blogs')
        
    @staticmethod    
    def update_blogs_cache():
        ManageBlog.update_news_blog()
        ManageBlog.update_all_blogs()
        
    @staticmethod    
    def update_news_blog():
        posts = []
        news_blog = feedparser.parse(settings.NEWS_BLOG_URL)
        for index in xrange(len(news_blog['entries'])):
            post = Post()
            date_str = news_blog.entries[index].date
            time_struct = time.strptime(date_str, "%a, %d %b %Y %H:%M:%S +0000")#str to time struct
            post.date = datetime.fromtimestamp(mktime(time_struct))
            post.title = news_blog.entries[index].title
            post.link = news_blog.entries[index].link
            post.content = news_blog.entries[index].content[0].value
            post.author = news_blog.entries[index].author
            post.blog_url = news_blog['feed']['link']
            posts.append(post)
        cache.set('news_blog', posts, settings.BLOGS_CACHE_TIME)
    
    @staticmethod    
    def update_all_blogs():
        more_blogs = []
        for blog in settings.MORE_BLOGS_URL:
            more_blogs.append(feedparser.parse(blog))
        
        more_blogs_posts = []
        for blog in more_blogs:
            for index in xrange(len(blog['entries'])):
                post = Post()
                date_str = blog.entries[index].date
                time_struct = time.strptime(date_str, "%a, %d %b %Y %H:%M:%S +0000")#str to time struct
                post.date = datetime.fromtimestamp(mktime(time_struct))
                post.title = blog.entries[index].title
                post.link = blog.entries[index].link
                post.set_content(blog.entries[index].content[0].value, cut_out=True)
                post.author = blog.entries[index].author
                post.blog_url = blog['feed']['link']
                more_blogs_posts.append(post)
                
        
        more_blogs_posts.sort()
        more_blogs_posts.sort(cmp=lambda a,b: cmp(a.date,  b.date), reverse=False)
        more_blogs_posts.reverse()
        
        cache.set('all_blogs', more_blogs_posts, settings.BLOGS_CACHE_TIME)
        
    