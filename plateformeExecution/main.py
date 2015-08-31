from kivy.app import App
from kivy.factory import Factory
from kivy.uix.floatlayout import FloatLayout



class AglLayout(FloatLayout):
    """

    """
    action_bar_title = "AGL"

    def spec_on_select(self):
        print "row_selected"

    def quit(self):
        AglApp().stop()


class AglApp(App):
    """

    """
    def build(self):
        self.root = AglLayout()

