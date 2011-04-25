from django.core.cache import cache
from osweb import settings
import urllib2
from xml.dom.minidom import parseString


class ManageProject():
    
    @staticmethod
    def get_projects():
        """Get a list of projects. 
        A project is a list of parameters: [name, 
                    shortname, shortdesc, description, 
                    homepage, downloadpage, languages, 
                    url_screenshot]
        """
        if cache.get('projects') is None:
            ManageProject.update_projects()
        return cache.get('projects')
        
    
        
    @staticmethod    
    def update_projects():
        
        projects = []
        for prj in settings.PROJECTS_INFO:
            element = []
            url_doap = prj[0]
            file = urllib2.urlopen(url_doap)
            data = file.read()
            file.close()
            dom = parseString(data)
            
            xmlTag = dom.getElementsByTagName('name')[0]
            element.append(xmlTag.childNodes[0].data)#name
            
            xmlTag = dom.getElementsByTagName('shortname')[0]
            element.append(xmlTag.childNodes[0].data)#shortname
            
            xmlTag = dom.getElementsByTagName('shortdesc')[0]
            element.append(xmlTag.childNodes[0].data)#shortdesc
            
            xmlTag = dom.getElementsByTagName('description')[0]
            element.append(xmlTag.childNodes[0].data)#description
            
            xmlTag = dom.getElementsByTagName('homepage')[0]
            element.append(xmlTag.getAttribute('rdf:resource'))#homepage
            
            xmlTag = dom.getElementsByTagName('download-page')[0]
            element.append(xmlTag.getAttribute('rdf:resource'))#downloadpage
            
            languages = []
            for xmlTag in dom.getElementsByTagName('programming-language'):
                lang = xmlTag.childNodes[0].data
                languages.append(lang)
            element.append(languages)#programming-languages
            element.append(prj[1])#url_screenshot            
            
            projects.append(element)
        
        cache.set('projects', projects, settings.PROJECTS_CACHE_TIME)
        
        
        


