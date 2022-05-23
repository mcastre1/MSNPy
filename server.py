import socket
import threading

HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
PORT = 5050 # Port used to talk to each client through.
SERVER = socket.gethostbyname(socket.gethostname()) # Get the local ip address.
ADDR = (SERVER, PORT) # Tuple for socket binding.

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create socket
server.bind(ADDR) # Binding the address and port to the socket server

MESSAGES = []

# Handles communication between client and server
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True

    while connected:
        # We first make sure we know the length of the message being received.
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False
                continue

            print(f"[{addr}] {msg}")
            MESSAGES.append(f'<addr>{addr}</addr>!{msg}')
            print(MESSAGES)
            conn.send("Msg received".encode(FORMAT))

    conn.close()

# Places the server socket into the listening mode.
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept() # This line waits for new connection and retrives info.
        thread = threading.Thread(target= handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}") # Show active connections

print("[STARTING] Server is starting...")
start()