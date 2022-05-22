from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

class MainScreen(Widget):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

    def say_hello(self):
        #print("Hello World")
        #self.ids.my_text.text = "Hi" # This is how we access the ids from a kv file.
        if self.ids.my_text.text: # Check if there is actually something in the text box before sending.
            print(self.ids.my_text.text)
            self.ids.my_text.text = ""
        

class ClientApp(App):
    def build(self):
        return MainScreen()

if __name__ == "__main__":
    ClientApp().run()