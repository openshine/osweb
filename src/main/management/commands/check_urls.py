from django.core.management.base import NoArgsCommand
from nannycentral.utils.urls import check_urls
from nannycentral.utils import log




class Command(NoArgsCommand):
    help = """
    check all medals criteria.
    """
    @flag_decorator
    def handle_noargs(self, **options):
        
        msg = "SCRIPT - 'check_urls' - start" 
        log.info(msg)
        
        try:
            check_urls()
        except:
            msg = "SCRIPT - 'check_urls' - error" 
            log.error(msg)  
        msg = "SCRIPT - 'check_urls' - end" 
        log.info(msg)
        
        
