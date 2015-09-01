from kivy.app import App
import os
import psutil
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from plateformeExecution.singleton import Singleton
from project import Project

import subprocess
from program import Program


class AttributeContainer(object):
    """
    Class that keeps current project's attributes
    This class is a Singleton
    """
    __metaclass__ = Singleton

    current_project = None


class ProjectScreen(Screen):
    """
        First page of the agl to appear
    """
    project_name = "New project"
    root_path = "C:\\AGL\\Projects"

    def init_root_path(self):
        """
        Create root_path if it doesn't already exists
        :return: void
        """
        if not os.path.isdir(self.root_path):
            os.makedirs(self.root_path)
            print "root_path's folder {} has been created".format(self.root_path)
        else:
            print "root_path {} exists".format(self.root_path)

    def init_project(self):
        """
        Initiate the Project's object
        :return: void
        """
        self.init_root_path()
        # set parameters for Project's constructor (feel free to add more)
        kwargs = {'project_name': self.project_name,
                  'root_path': self.root_path}
        new_project = Project(**kwargs)
        new_project.create_folder()
        AttributeContainer().current_project = new_project


class MainScreen(Screen):
    action_bar_title = "AGL"
    dia_path = 'C:\\Program Files (x86)\\Dia\\bin\\dia.exe'
        
    def launch_dia(self):
        is_running = False
        for p in psutil.process_iter():
            try:
                if p.name() == 'dia.exe':
                    print "dia is already running"
                    is_running = True
            except psutil.error:
                pass
        if not is_running:
            dia = Program(self.dia_path)
            dia.start()
            print "program {} started".format(self.dia_path)

    def spec_on_select(self):
        print "row_selected" 

    def get_specification_filenames(self):
        """
        list all use-cases's filenames
        :return: a list of filenames
        """
        project = AttributeContainer().current_project
        use_cases = []
        print "project: {}".format(project)
        if project is not None:
            print "project is not none"
            use_cases = project.get_specification_files()
            print "specification filenames: {}".format(use_cases)

        return use_cases


class ScreenManagement(ScreenManager):
    pass
        

class AglApp(App):
    def build(self):
        return Builder.load_file("agl.kv")

if __name__ == '__main__':
    AglApp().run()