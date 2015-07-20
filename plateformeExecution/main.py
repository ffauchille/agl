from kivy.app import App
from kivy.factory import Factory
from kivy.uix.floatlayout import FloatLayout



class AglLayout(FloatLayout):
    """

    """
    action_bar_title = "AGL"

    def quit(self):
        AglApp().stop()


class AglApp(App):
    """

    """
    def build(self):
        self.root = AglLayout()


if __name__ == '__main__':
    AglApp().run()