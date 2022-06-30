
import socket
clients = []

#c.sendall(str(client_id).encode())

class ClientHandler:

    def __init__(self, client, address, ID):
        self.client = client
        self.address = address
        self.ID = ID

    def send(self, data):
        self.client.send(str(data).encode())

    def recv(self):
        return self.client.recv(1024).decode()

    def close(self):
        self.client.close()


def sendAll(data):
    for client in clients:
        client.send(data)

def closeAll():
    for client in clients:
        client.close()


if __name__ == "__main__":
    
    port = 19487 
   
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    s.bind((host, port))  
    s.listen(5)  
    m = ""

    print("Server {} listening @ {}:{}".format(s, host, port))

    while True:
        
        c, addr = s.accept()  
        print("Connection from " + str(c) + ":" + str(addr) + " has been established.")

        client_id = len(clients) + 1
        clients.append(ClientHandler(c, addr, client_id))

        messages = []

        for client in clients:
            print("Client {}: {}".format(client.ID, client.recv()))
            messages.append(client.recv())
        
        if(len(messages) > 0):
            sendAll(messages[0])
            if(messages[0] == "quit"):
                closeAll()
                break
            messages.pop(0)

        c.close()
        print("Connection from " + str(c) + ":" + str(addr) + " has been closed.")
        clients.remove(c)
        print("Client {} has been removed from the list.".format(c))
        print("Clients in the list: {}".format(clients))
        print("\n")

    s.close()
    print("Server {} has been closed.".format(s))
    print("Clients in the list: {}".format(clients))
