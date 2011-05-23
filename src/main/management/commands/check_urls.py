#osweb. Main Openshines website 
#Copyright (C) 2011  Openshine sl
# Authors:
#    Pablo Vieytes <pvieytes@openshine.com>
#    Roberto Majadas <roberto.majadas@openshine.com>
#    Cesar Garcia Tapia <cesar.garcia.tapia@openshine.com>
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.


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
        
        
