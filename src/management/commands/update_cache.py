from django.core.management.base import NoArgsCommand
from osweb.blogs import ManageBlog
from osweb.twitter import ManageTwitter

class Command(NoArgsCommand):
    help = """
    check automatic rehabs.
    """
    def handle_noargs(self, **options):
        ManageTwitter.update_tweets_cache()
        ManageBlog.update_blogs_cache()
