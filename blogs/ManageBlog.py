from django.core.cache import cache


class ManageBlog():
    
    
    @staticmethod
    def get_home_page_blog():
        return "home blog"
    
    
    @staticmethod
    def get_all_blogs():
        return "blogs"