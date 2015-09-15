import os
from kivy.uix.treeview import TreeView
import psutil

from kivy.app import App
from kivy.properties import ObjectProperty, DictProperty, Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import WidgetException
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from singleton import Singleton
from project import Project
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

    def init_all(self, project_name):
        """
        Function launched after the user click on "Creer projet"
        :return: void
        """
        self.init_project(project_name)

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


class RefTreeWidget(FloatLayout):
    """
    Widget for the referentiel tree view
    """
    # Properties attributes
    tree_changes = DictProperty({})
    # Regular attributes
    tree_view = TreeView()

    def __init__(self, **kwargs):
        super(RefTreeWidget, self).__init__(**kwargs)
        # update_tree will be call each second (1 times per second)
        Clock.schedule_interval(self.update_ref, 1 / 0.2)

    def update_tree(self):
        """
        In order to refresh the layout, we remove the former widget
        and add a new one.
        We also parse all .dia files in other to get all new elements the user created
        :return: void
        """
        try:
            self.remove_widget(self.tree_view)
        except WidgetException:
            pass

        if AttributeContainer().current_project is not None:
            project = AttributeContainer().current_project
            if AttributeContainer().current_project.current_ref is not None:
                ref = project.get_ref()
                self.tree_view = ref.referentiel_tree
                try:
                    # we remove the referentiel TreeView Widget for *this* FloatLayout
                    self.add_widget(self.tree_view)
                except WidgetException:
                    pass

    def update_ref(self, dt = None):
        """
        NOTE: This method is called every seconds.

        :param dt: delta time required for the Clock.schedule_interval
        :return:
        """
        if AttributeContainer().current_project is not None:
            project = AttributeContainer().current_project
            project.update_specifications()
            # TODO : Need to update all the other parts of the referentiel (conception, realisation, ...)
            self.update_tree()


class ScreenManagement(ScreenManager):
    pass


class AglApp(App):
    def build(self):
        return Builder.load_file("agl.kv")

if __name__ == '__main__':
    AglApp().run()