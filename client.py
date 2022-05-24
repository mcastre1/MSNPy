from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.core.window import Window
import socket
import threading

# Infomartion needed for connecting to the server ##
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = '192.168.1.15'
ADDR = (SERVER, PORT)
####################################################

# Connecting client to server ##########
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
########################################

"""
Client GUI class.
"""
class MainScreen(Widget):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        Window.bind(on_request_close=self.end_func) # Binding the close button on a window to a function (end_func)
        self.thread = threading.Thread(target=self.receive_messages) # Thread used for receiving messages from the server.
        self.thread.start()

    def receive_messages(self):
        while True:
            #print(client.recv(2048).decode(FORMAT))
            self.ids.text_in.text = self.ids.text_in.text + client.recv(2048).decode(FORMAT)
    
    # Takes care of window close button event.
    # Will send disconnect message to server to make sure we disconnect from server properly.
    def end_func(self, *args):
        self.send(DISCONNECT_MESSAGE)
        Window.close()

    # Intermediary function to send a message to the server.
    def send_message(self):
        msg = self.ids.my_text.text
        self.send(msg)

    # Sends message to server.
    def send(self,msg):
        if self.ids.my_text.text:
            message = msg.encode(FORMAT) # Encode into byte format first.
            msg_length = len(msg)
            send_length = str(msg_length).encode('utf-8')
            send_length += b' ' * (HEADER - len(send_length)) # Pads message length to make sure it folows the HEADER/FORMAT of 64 in this case.
            client.send(send_length)
            client.send(message)

            self.ids.my_text.text = ""

            #print(client.recv(2048).decode(FORMAT))
        
"""
App class for Kivy dev.
"""
class ClientApp(App):
    def build(self):
        return MainScreen()

if __name__ == "__main__":
    ClientApp().run()