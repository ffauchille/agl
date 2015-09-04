from kivy.adapters.listadapter import ListAdapter
from kivy.app import App
import os
from kivy.event import EventDispatcher
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.listview import ListItemButton
from kivy.uix.treeview import TreeViewLabel, TreeView
import psutil
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from singleton import Singleton
from project import Project
from program import Program
from ref import Reference
from referentiel.passerrelles.use_case import UsecaseParser


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

    def init_all(self, project_name):
        """
        Function launched after the user click on "Creer projet"
        :return: void
        """
        self.init_project(project_name)
        us = UsecaseParser()
        project = AttributeContainer().current_project
        use_cases = us.parse(project.get_specification_files())

        ref = Reference(project.absolute_path)
        ref.insert_use_cases(use_cases)

    def init_project(self, value):
        """
        Initiate the Project's object
        :return: void
        """
        self.init_root_path()
        # set parameters for Project's constructor (feel free to add more)
        kwargs = {'project_name': value,
                  'root_path': self.root_path}
        new_project = Project(**kwargs)
        new_project.create_folder()
        AttributeContainer().current_project = new_project


class SpecificationListener(EventDispatcher):
    """
    Handle changes from this project's specification directory
    """
    specifications = ListProperty([])


def populate_tree(tree_view, parent, node):
    if parent is None:
        tree_node = tree_view.add_node(TreeViewLabel(text=node['node_id'], is_open=True))
    else:
        tree_node = tree_view.add_node(TreeViewLabel(text=node['node_id'], is_open=True), parent)

    for child_node in node['children']:
        populate_tree(tree_view, tree_node, child_node)


referentiel_tree = {'node_id': '1',
                    'children': [{'node_id': '1.1',
                                  'children': [{'node_id': '1.1.1',
                                                'children': [{'node_id': '1.1.1.1',
                                                              'children': []}]},
                                               {'node_id': '1.1.2',
                                                'children': []},
                                               {'node_id': '1.1.3',
                                                'children': []}]},
                                 {'node_id': '1.2',
                                  'children': []}]}


class MainScreen(Screen):
    action_bar_title = "AGL"
    dia_path = 'C:\\Program Files (x86)\\Dia\\bin\\dia.exe'
    specs = SpecificationListener().specifications

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


def get_ref_tree():
    tv = TreeView(root_options=dict(text='Root project'),
                  hide_root=False,
                  indent_level=5)

    populate_tree(tv, None, referentiel_tree)
    print "tree returned : {}".format(tv.get_root())
    return tv


class RefTreeWidget(FloatLayout):
    """

    """
    tree_changes = ObjectProperty(referentiel_tree)

    def __init__(self, **kwargs):
        super(RefTreeWidget, self).__init__(**kwargs)
        tv = get_ref_tree()
        self.add_widget(tv)

    def on_tree_changes(self):
        print "tree changed"


class ScreenManagement(ScreenManager):
    pass


class AglApp(App):
    def build(self):
        return Builder.load_file("agl.kv")


if __name__ == '__main__':
    AglApp().run()
