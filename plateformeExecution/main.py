import os
from kivy.uix.treeview import TreeView
import psutil

from kivy.app import App
from kivy.properties import ObjectProperty, Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import WidgetException
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from singleton import Singleton
from project import Project
from program import Program
from flowchart_to_code import FlowchartToCode
from referentiel.passerelles.diatosql import JavaParserSQL


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
    intellij_path = 'C:\\Program Files (x86)\\JetBrains\\IntelliJ IDEA 14.1.3\\bin\\idea.exe'
    f2c_path =  'C:\\Program Files (x86)\\AthTek\\FlowchartToCode\\FlowchartToCode.exe'
    # IDs in kv
    ref_tree_widget = ObjectProperty(None)

    def launch_dia(self):
        is_running = False
        for p in psutil.process_iter():
            try:
                if p.name() == 'dia.exe':
                    print "Dia is already running"
                    is_running = True
            except psutil.error:
                pass
        if not is_running:
            dia = Program(self.dia_path)
            dia.start()
            print "program {} started".format(self.dia_path)

    def launch_intellij(self):
        is_running = False
        for p in psutil.process_iter():
            try:
                if p.name() == 'idea.exe':
                    print "IntelliJ IDEA is already running"
                    is_running = True
            except psutil.error:
                pass
        if not is_running:
            intellij = Program(self.intellij_path)
            intellij.start()
            print "program {} started".format(self.intellij_path)

    def launch_f2c(self):
        is_running = False
        for p in psutil.process_iter():
            try:
                if p.name() == 'FlowchartToCode.exe':
                    print "Flowchart To Code is already running"
                    is_running = True
            except psutil.error:
                pass
        if not is_running:
            f2c = Program(self.f2c_path)
            f2c.start()
            print "program {} started".format(self.f2c_path)

    def launch_mergeScript(self):
            mergeScript = FlowchartToCode()
            project = AttributeContainer().current_project
            mergeScript.implement(project.get_realisation_files())
            print "program {} started".format('Merge script running...')

    def launch_generateSQL(self):
        diatosql = JavaParserSQL()
        sql_file = diatosql.parse("")
        print "Table generated in file : " + sql_file

class RefTreeWidget(FloatLayout):
    """
    Widget for the referentiel tree view
    """
    # Regular attributes
    tree_view = TreeView()

    def __init__(self, **kwargs):
        super(RefTreeWidget, self).__init__(**kwargs)
        # update_tree will be call each 4 seconds
        # FIXME The line below has to be uncommented after fixing the reference duplication BUG!
        Clock.schedule_interval(self.update_ref, 4)

    def refresh_widget(self):
        """
        Refresh the referentiel layout
        :return:
        """
        try:
            self.clear_widgets()
            self.add_widget(self.tree_view)
            print "widgets refreshed"
        except WidgetException as e:
            print "clear widgets error : {}".format(e.message)

    def update_tree(self):
        """
        In order to refresh the layout, we remove the former widget
        and add a new one.
        We also parse all .dia files in other to get all new elements the user created
        :return: void
        """

        if AttributeContainer().current_project is not None:
            project = AttributeContainer().current_project
            if AttributeContainer().current_project.current_ref is not None:
                try:
                    self.clear_widgets()
                    ref = project.get_ref()
                    ref.load_json()
                    self.tree_view = ref.get_ref_tree()
                    self.add_widget(self.tree_view)
                except WidgetException as e:
                    print "update_tree error: {}".format(e.message)

    def update_ref(self, dt = None):
        """
        NOTE: This method is called every seconds.

        :param dt: delta time required for the Clock.schedule_interval
        :return: void
        """
        if AttributeContainer().current_project is not None:
            project = AttributeContainer().current_project
            # changed_x check if something changed, if so update the widget
            changed_s = project.update_specification()
            changed_c = project.update_conception()
            # TODO : Need to update all the other parts of the referentiel (conception, realisation, ...)

            if changed_c == 1 or changed_s == 1:
                self.update_tree()
                print "Le referentiel a ete modifie !"
            else:
                print "Pas de modification detectee.."

    def first_update(self):
        """
        This method is called only "once"
        :return:
        """
        if AttributeContainer().current_project is not None:
            project = AttributeContainer().current_project
            # changed_x check if something changed, if so update the widget
            project.update_specification()
            project.update_conception()
            project.update_realisation()
            # TODO : Need to update all the other parts of the referentiel (conception, realisation, ...)

            self.update_tree()


class ScreenManagement(ScreenManager):
    pass


class AglApp(App):
    title = 'AGL'
    def build(self):
        return Builder.load_file("agl.kv")

if __name__ == '__main__':
    AglApp().run()