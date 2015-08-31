from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
import psutil
import subprocess
from program import Program


class AglLayout(FloatLayout):
    action_bar_title = "AGL"
    dia_path = 'C:\\Program Files (x86)\\Dia\\bin\\dia.exe'

    def quit(self):
        AglApp().stop()
        
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


class AglApp(App):
    def build(self):
        self.root = AglLayout()


if __name__ == '__main__':
    AglApp().run()