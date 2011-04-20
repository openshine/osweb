from django.core.cache import cache
from osweb import settings
import time
import feedparser

class ManageBlog():
    
    @staticmethod
    def get_home_page_blog():
        if cache.get('home_blog') is None:
            ManageBlog.__update_home_blog()
        return cache.get('home_blog')
        
    @staticmethod    
    def get_all_blogs():
        if cache.get('all_blogs') is None:
            ManageBlog.__update_all_blogs()
        return cache.get('all_blogs')
        
    @staticmethod    
    def update_blogs():
        ManageBlog.__update_home_blog()
        ManageBlog.__update_all_blogs()
        
    @staticmethod    
    def __update_home_blog():
        #home blog
        home_posts = []
        home_blog = feedparser.parse(settings.HOME_PAGE_BLOG_URL)
        for index in xrange(len(home_blog['entries'])):
            entry = []
            date_str = str(home_blog.entries[index].date)
            entry.append(time.strptime(date_str, "%a, %d %b %Y %H:%M:%S +0000"))#str to time struct
            entry.append(date_str)
            entry.append(str(home_blog.entries[index].title))
            entry.append(str(home_blog.entries[index].link))
            entry.append(str(home_blog.entries[index].content[0].value))
            home_posts.append(entry)
        cache.set('home_blog', home_posts, settings.BLOGS_CACHE_TIME)
    
    @staticmethod    
    def __update_all_blogs():
        more_blogs = []
        for blog in settings.MORE_BLOGS_URL:
            more_blogs.append(feedparser.parse(blog))
        
        more_blogs_posts = []
        for blog in more_blogs:
            for index in xrange(len(blog['entries'])):
                entry = []
                date_str = str(blog.entries[index].date)
                entry.append(time.strptime(date_str, "%a, %d %b %Y %H:%M:%S +0000"))#str to time struct
                entry.append(date_str)
                entry.append(str(blog.entries[index].title))
                entry.append(str(blog.entries[index].link))
                entry.append(str(blog.entries[index].content[0].value))
                more_blogs_posts.append(entry)
        
        more_blogs_posts.sort()
        more_blogs_posts.reverse()
        cache.set('all_blogs', more_blogs_posts, settings.BLOGS_CACHE_TIME)
        
    