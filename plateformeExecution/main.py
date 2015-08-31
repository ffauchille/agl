from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
import psutil
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

import subprocess
from program import Program

class ProjectScreen(Screen):
    pass

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

class ScreenManagement(ScreenManager):
    pass
        

class AglApp(App):
    def build(self):
        return Builder.load_file("agl.kv")

if __name__ == '__main__':
    AglApp().run()