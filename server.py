
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

    print("Server {} listening @ {}:{}".format(s, host, port))

    while True:
        
        c, addr = s.accept()  

        client_id = len(clients) + 1
        clients.append(ClientHandler(c, addr, client_id))

        m = c.recv(1024).decode() 

        g = {
            "host" : clients[0].address,
            "host_id" : clients[0].ID,
        }

        print("Connection from " + str(c) + ":" + str(addr) + " has been established.")
        print("Host", str(clients[0].client), ": Address", str(clients[0].address))
        print("Request:\t", str(m))
        
        if(str(m) == "quit" and addr[0] == clients[0].address[0]):
            closeAll();
            break;

        if(str(m) == "get"):
            clients[0].send(g)
            

        

