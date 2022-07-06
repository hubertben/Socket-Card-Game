
import socket
from threading import Thread
import signal
import os


class GameState:


    def __init__(self):
        self.g = {}

    def __str__(self):
        return str(self.g)



class Client:

    def __init__(self, port, address):
        self.port = port
        self.address = address

        self.has_id = False

    def __str__(self):
        return "Client: " + str(self.port) + " | " + str(self.address)

    def send(self, message):
        self.port.send(str(message).encode())


chatLog = []

class ClientHandler:

    def __init__(self):
        self.clients = []

    def add(self, client):
        t = Thread(target=self.handle, args=(client,))
        t.start()
        self.clients.append(client)

    def handle(self, client):

        while True:
            data = client.port.recv(1024).decode()

            print("[SERVER-LOG]: [" + str(data) + "]")

            if not data:
                client.port.close()
                continue

            if data == "quit":
                os.kill(os.getpid(), signal.SIGINT)

            chatLog.append(data)
            self.broadcast(chatLog)


    def broadcast(self, message):
        for client in self.clients:
            client.send(message)


s = None
handler = ClientHandler()
gameState = GameState()


if __name__ == "__main__":

    port = int(input("Enter port number: "))
    host = socket.gethostname()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((host, port))
    s.listen(5)

    print("Server listening @ {}:{}".format(host, port))

    while True:

        port, addr = s.accept()

        client = Client(port, addr)
        print("Client connected: " + str(client))

        handler.add(client)


    # s.close()
    # print("Server closed")
    # exit()
