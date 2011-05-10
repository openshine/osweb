from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    help = """
    check automatic rehabs.
    """
    def handle_noargs(self, **options):
       print "update cache" 
