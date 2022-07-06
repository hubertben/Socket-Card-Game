
import socket
from threading import Thread
import random

shutdown = False


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

            print("[SERVER-LOG]: [" + str(data) + "]")

            if not data:
                break

            if data == "quit":
                shutdown = True
                break

            print(data)
            state.append(data)
            client.send(state)

        
        client.send("Server shutting down...", shutdown)
        client.port.close()

    


s = None
handler = ClientHandler()


if __name__ == "__main__":
    
    port = int(input("Enter port number: "))
    host = socket.gethostname()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((host, port))  
    s.listen(5)

    print("Server listening @ {}:{}".format(host, port))

    while True:

        port, addr = s.accept() 

        if(shutdown):
            print("Server shutting down...")
            break

        client = Client(port, addr)
        print("Client connected: " + str(client))

        handler.add(client)

    s.close()
    print("Server closed")
    exit()
    



    