from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

class MainScreen(Widget):
    pass

class ClientApp(App):
    def build(self):
        return MainScreen()

if __name__ == "__main__":
    ClientApp().run()