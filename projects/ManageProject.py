from django.core.cache import cache
from osweb import settings
import urllib2
from xml.dom.minidom import parseString
from django.template.defaultfilters import slugify


class ManageProject():
    
    @staticmethod
    def get_projects():
        """Return a list of projects. 
        A project is a list of parameters: [name, slugname,
                    shortname, shortdesc, description, 
                    homepage, downloadpage, languages, 
                    url_screenshot]
        """
        project_names = cache.get('project_names')
        if project_names is None:
            ManageProject.update_projects_cache()
            project_names = cache.get('project_names')
        projects = []
        for project_name in project_names:
            project = cache.get(project_name)
            if project is None:
                ManageProject.update_projects_cache()
                project = cache.get(project_name)
            projects.append(project)
        return projects
    
    
    
    @staticmethod   
    def get_project(projectname):
        project = cache.get(projectname)
        if project is None:  
            ManageProject.update_projects_cache()
            return cache.get(projectname)
        return project
            
            
            
    @staticmethod
    def update_projects_cache():
        project_names =[]
        projects = ManageProject.read_projects()
        for project in projects:
            slug_name = project[1] 
            project_names.append(slug_name)
            cache.set(slug_name, project, settings.PROJECTS_CACHE_TIME)
        cache.set('project_names', project_names, settings.PROJECTS_CACHE_TIME)
            
            
        
        
    @staticmethod    
    def read_projects():
        """Return a list of projects. 
        A project is a list of parameters: [name, slugname,
                    shortname, shortdesc, description, 
                    homepage, downloadpage, languages, 
                    url_screenshot]""" 
                    
        projects = []
        for prj in settings.PROJECTS_INFO:
            element = []
            url_doap = prj[0]
            file = urllib2.urlopen(url_doap)
            data = file.read()
            file.close()
            dom = parseString(data)
            
            xmlTag = dom.getElementsByTagName('name')[0]
            name = xmlTag.childNodes[0].data
            element.append(name)#name
            
            element.append(slugify(name))#slugname
            
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
        
        return projects
    
        
        
        


