from kivy.app import App
from kivy.factory import Factory
from kivy.uix.floatlayout import FloatLayout

import subprocess



class AglLayout(FloatLayout):
    """

    """
    action_bar_title = "AGL"

    def quit(self):
        AglApp().stop()

    def launch_notepad(self):
        subprocess.Popen('C:\Windows\System32\notepad.exe')


class AglApp(App):
    """

    """
    def build(self):
        self.root = AglLayout()


if __name__ == '__main__':
    AglApp().run()