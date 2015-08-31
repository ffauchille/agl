from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.


# Declare both screens
class ProjectScreen(Screen):
    pass

class MainScreen(Screen):
    action_bar_title = "AGL"

class ScreenManagement(ScreenManager):
    pass

class AglApp(App):

    def build(self):
        return Builder.load_file("agl.kv")

if __name__ == '__main__':
    AglApp().run()