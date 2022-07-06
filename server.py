
import socket
from threading import Thread
import random

SHUTDOWN = False


class Client:

    def __init__(self, port, address):
        self.port = port
        self.address = address

        self.has_id = False

    def __str__(self):
        return "Client: " + str(self.port) + " | " + str(self.address)

    def send(self, message):
        self.port.send(str(message).encode())
        

   

state = []

class ClientHandler:


    def __init__(self):
        pass
        
    def add(self, client):
        t = Thread(target = self.handle, args = (client,))
        t.start()

    def handle(self, client):
        while True:
            data = client.port.recv(1024).decode()

            if not data:
                break

            if data == "quit":
                SHUTDOWN = True
                client.send("Server shutting down...")
                client.port.close()
                break

            print(data)
            state.append(data)
            client.send(state)

    


s = None
handler = ClientHandler()


if __name__ == "__main__":
    
    port = int(input("Enter port number: "))
    host = socket.gethostname()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((host, port))  
    s.listen(5)

    print("Server listening @ {}:{}".format(host, port))

    while True or SHUTDOWN:

        port, addr = s.accept() 

        client = Client(port, addr)
        print("Client connected: " + str(client))

        handler.add(client)


    s.close()

        



    



    