from kivy.adapters.listadapter import ListAdapter
from kivy.app import App
import os

from kivy.app import App
from kivy.event import EventDispatcher
from kivy.properties import ListProperty, ObjectProperty, DictProperty, NumericProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.treeview import TreeViewLabel, TreeView
from kivy.uix.widget import WidgetException
import psutil
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from singleton import Singleton
from project import Project
from program import Program
from referentiel.ref import Reference

class AttributeContainer(object):
    """
    Class that keeps current project's attributes
    This class is a Singleton
    """
    __metaclass__ = Singleton

    current_project = None

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
        AttributeContainer().current_project.update_specs()

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


class MainScreen(Screen):
    action_bar_title = "AGL"
    dia_path = 'C:\\Program Files (x86)\\Dia\\bin\\dia.exe'
    # IDs in kv
    ref_tree_widget = ObjectProperty(None)

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


class RefTreeWidget(FloatLayout):
    """
    Widget for the referentiel tree view
    """
    tree_changes = DictProperty(AttributeContainer().referentiel_tree)
    tree_view = TreeView()

    def __init__(self, **kwargs):
        super(RefTreeWidget, self).__init__(**kwargs)
        self.update_tree()

    def change_ref(self):
        self.tree_changes = dict({'node_id': 'new 1',
                                  'children': [{'node_id': 'new 1.1',
                                                'children': []
                                                }]
                                  })

    def update_tree(self):
        """
            In order to refresh the layout, we remove the former widget
            and add the new one.
        """
        try:
            self.remove_widget(self.tree_view)
        except WidgetException:
            pass
        project_name = 'New project'

        if AttributeContainer().current_project is not None:
            project_name = AttributeContainer().current_project.name

        self.tree_view = TreeView(root_options=dict(text=project_name),
                                  hide_root=False,
                                  indent_level=5)
        populate_tree(self.tree_view, None, self.tree_changes)
        self.add_widget(self.tree_view)

    def on_tree_changes(self, instance, value):
        print "referentiel tree has changed"
        self.update_tree()


class ScreenManagement(ScreenManager):
    pass

class AglApp(App):
    def build(self):
        return Builder.load_file("agl.kv")

if __name__ == '__main__':
    AglApp().run()
