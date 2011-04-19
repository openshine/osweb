from django.core.cache import cache
from osweb import settings
 
import feedparser


class ManageBlog():
    
    
    @staticmethod
    def get_home_page_blog():
        if cache.get('home_blog') is None:
            ManageBlog.update_blogs()
        return cache.get('home_blog')
        
        
    @staticmethod
    def get_all_blogs():
        if cache.get('all_blogs') is None:
            ManageBlog.update_blogs()
        return cache.get('all_blogs')
        
        
    @staticmethod
    def update_blogs():
        #home blog
        home_posts = []
        home_blog = feedparser.parse(settings.HOME_PAGE_BLOG_URL)
        for index in xrange(len(home_blog['entries'])):
            if index >= settings.NUM_HOME_NEWS:
                break
            entry = []
            entry.append(str(home_blog.entries[index].date))
            entry.append(str(home_blog.entries[index].title))
            entry.append(str(home_blog.entries[index].link))
            entry.append(str(home_blog.entries[index].content[0].value))
            home_posts.append(entry)
        
        cache.set('home_blog', home_posts, settings.BLOGS_CACHE_TIME)
        
        
        
        more_blogs = []
        for blog in settings.MORE_BLOGS_URL:
            more_blogs.append(feedparser.parse(blog))
        cache.set('all_blogs', 'all_blogs updated', settings.BLOGS_CACHE_TIME)
        
        
        
        
   