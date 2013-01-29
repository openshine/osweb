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
    def get_frontpage_projects():
        """Return a list of Project instances.
        """
        projects = []
        for prj_dict in ProjectsData:
            project = Project(prj_dict)
            if prj_dict['frontpage']:
                projects.append(project)
        return projects
    
    @staticmethod
    def get_no_frontpage_projects():
        """Return a list of Project instances.
        """
        projects = []
        for prj_dict in ProjectsData:
            project = Project(prj_dict)
            if  prj_dict['frontpage'] == False:
                projects.append(project)
        return projects
    
    
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
        
        
        
        
