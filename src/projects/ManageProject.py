from django.template.defaultfilters import slugify
from osweb.projects.projects_data import ProjectsData


class Project():
    name = None
    slug_name = None
    description = None
    shortdesc = None
    homepage = None
    downloadpage = None
    screenshot = None
    logo = None
    
    def __init__(self, dict):
        self.name = dict['name']
        self.slug_name = slugify(self.name)
        self.description = dict['description']
        self.shortdesc = dict['shortdesc']
        self.homepage = dict['homepage']
        self.downloadpage = dict['downloadpage']
        self.screenshot = dict['screenshot']
        self.screenshot_small = dict['screenshot_small']
        self.logo = dict['logo']
    
    
    
class ManageProject():
    
    @staticmethod
    def get_projects():
        """Return a list of Project instances.
        """
        projects = []
        for prj_dict in ProjectsData:
            project = Project(prj_dict)
            projects.append(project)
        return projects

    @staticmethod
    def get_project(slugname):
        """Return a Project instances.
        """
        for prj_dict in ProjectsData:
            if slugify(prj_dict['name']) == slugname:
                return Project(prj_dict)
        return None
        
        
        
        
