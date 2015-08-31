from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

import subprocess

class AglLayout(FloatLayout):
    action_bar_title = "AGL"

    def quit(self):
        AglApp().stop()
        
    def launch_dia(self):
        subprocess.call(['C:\\Program Files (x86)\\Dia\\bin\\dia.exe'])
        
    def spec_on_select(self):
        print "row_selected"

class AglApp(App):
    def build(self):
        self.root = AglLayout()


if __name__ == '__main__':
    AglApp().run()