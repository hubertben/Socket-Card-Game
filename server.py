
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

        m = c.recv(1024).decode()
        print("Message from client: " + str(m))

        c.send("Message from server: Received message from client: " + str(m))

        if(str(m) == "quit"):
            c.close()
            break

    s.close()

        
       
            
