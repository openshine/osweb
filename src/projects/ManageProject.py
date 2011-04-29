from django.core.cache import cache
from osweb import settings
import urllib2
from xml.dom.minidom import parseString
from django.template.defaultfilters import slugify

class Project():
    name = None
    slugname = None
    shortname = None
    shortdesc = None
    description = None
    homepage = None
    downloadpage = None
    languages = None
    url_screenshot = None
    
    
    
    
    
class ManageProject():
    
    @staticmethod
    def get_projects():
        """Return a list of Project's instances.
        """
        project_names = cache.get('project_names')
        if project_names is None:
            ManageProject.update_projects_cache()
            project_names = cache.get('project_names')#Array with the names of the cache for each project
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
            project_names.append(project.slugname)
            cache.set(project.slugname, project, settings.PROJECTS_CACHE_TIME)
        cache.set('project_names', project_names, settings.PROJECTS_CACHE_TIME)
            
            
        
        
    @staticmethod    
    def read_projects():
        """Return a list of Project's instances.""" 
                    
        projects = []
        for prj in settings.PROJECTS_INFO:
            #element = []
            project = Project()
            url_doap = prj[0]#doap url
            file = urllib2.urlopen(url_doap)
            data = file.read()
            file.close()
            dom = parseString(data)
            
            xmlTag = dom.getElementsByTagName('name')[0]
            project.name = xmlTag.childNodes[0].data
            
            
            project.slugname = slugify(project.name)#slugname
            
            xmlTag = dom.getElementsByTagName('shortname')[0]
            project.shortname = xmlTag.childNodes[0].data#shortname
            
            xmlTag = dom.getElementsByTagName('shortdesc')[0]
            project.shortdesc = xmlTag.childNodes[0].data#shortdesc
            
            xmlTag = dom.getElementsByTagName('description')[0]
            project.description = xmlTag.childNodes[0].data#description
            
            xmlTag = dom.getElementsByTagName('homepage')[0]
            project.homepage = xmlTag.getAttribute('rdf:resource')#homepage
            
            xmlTag = dom.getElementsByTagName('download-page')[0]
            project.downloadpage = xmlTag.getAttribute('rdf:resource')#downloadpage
            
            languages = []
            for xmlTag in dom.getElementsByTagName('programming-language'):
                lang = xmlTag.childNodes[0].data
                languages.append(lang)
            project.languages =languages#programming-languages
            
            project.url_screenshot = prj[1]#url_screenshot            
            
            projects.append(project)
        
        return projects
    
        
        
        


