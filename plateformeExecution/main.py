from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

import subprocess


# Declare both screens
class ProjectScreen(Screen):
    pass

class MainScreen(Screen):
    action_bar_title = "AGL"
    dia_path = 'C:\\Program Files (x86)\\Dia\\bin\\dia.exe'
    
    def launch_dia(self):
        subprocess.call([self.dia_path])
        
    def spec_on_select(self):
        print "row_selected"

class ScreenManagement(ScreenManager):
    pass
        

class AglApp(App):
    def build(self):
        return Builder.load_file("agl.kv")

if __name__ == '__main__':
    AglApp().run()