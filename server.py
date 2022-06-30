
import socket
clients = []

#c.sendall(str(client_id).encode())


class ClientHandler:

    def __init__(self, client, address, ID):
        self.client = client
        self.address = address
        self.ID = ID

        self.has_id = False

    def send(self, data):
        self.client.send(str(data).encode())

    def close(self):
        self.client.close()

    def __str__(self):
        return "Client: " + str(self.ID) + " " + str(self.address)


def sendAll(data):
    for client in clients:
        client.send(data)

def closeAll():
    for client in clients:
        client.close()

def checkClients(addr):
    for client in clients:
        if(client.address == addr):
            return True
    return False


def addClient(client, address, ID):
    c = ClientHandler(client, address, ID)
    clients.append(c)
    i = "$" + str(ID)
    c.send(str(i))
    c.has_id = True
    print(c)


if __name__ == "__main__":
    
    port = int(input("Enter port number: "))

    if(port < 1024 or port > 65535):
        port = 19487
   
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    s.bind((host, port))  
    s.listen(5)  
    m = ""
    client_id = 0

    print("Server {} listening @ {}:{}".format(s, host, port))

    while True:
        
        c, addr = s.accept()  
        print("Connection from " + str(c) + ":" + str(addr) + " has been established.")

        m = c.recv(1024).decode()
        
        if(not checkClients(addr)):
            addClient(c, addr, client_id)
            client_id += 1
            print("Client Added")

        print("Message from client: " + str(m))

        c.send("Message from server: Received message from client: " + str(m))
        c.close()

        if(str(m) == "quit"): 
            break

    s.close()

        


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.value + " of " + self.suit



class Player:
    def __init__(self, name, color, handler):
        self.name = name
        self.color = color
        self.hand = []

        self.handler = handler

    def __str__(self):
        return self.name + " has " + str(len(self.hand)) + " cards."

    def addCard(self, card):
        self.hand.append(card)

    def removeCard(self, card):
        self.hand.remove(card)



class BlackJack:

    def __init__(self):
        self.deck = []
        self.players = []
        self.state = {}

    def updateState(self):
        self.state["players"] = self.players
        

    def generateCards(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        for suit in suits:
            for value in values:
                self.deck.append(Card(suit, value))

    def shuffle(self):
        import random
        random.shuffle(self.deck)

    



    