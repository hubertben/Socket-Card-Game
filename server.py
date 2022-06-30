
import socket
clients = []
from threading import Thread



class ClientHandler:

    def __init__(self, client, address, ID):
        self.client = client
        self.address = address
        self.ID = ID

        self.has_id = False

    def send(self, data):
        self.client.send(str(data).encode())

    def __str__(self):
        return "Client: " + str(self.ID) + " " + str(self.address)


def sendAll(data):
    for c in clients:
        c.send(data)


def checkClients(addr):
    for c in clients:
        if(c.address[0] == addr[0]):
            return c
    return False


def addClient(client, address, ID):
    c = ClientHandler(client, address, ID)
    clients.append(c)
    c.has_id = True

    i = "$" + str(ID)
    client.send(str(i))
    print("Client " + str(ID) + " connected")




def command(c, message):

    message = message[1:].split(" ")
    print("From " + str(c) + ": ")
    print(message)

    if(str(message[0]) == "kill"):
        exit()

    if(str(message[0]) == "sendall"):
        print("Sending to all: " + str(message[1]))
        sendAll(str(message[1]))
        return

   

if __name__ == "__main__":
    
    port = int(input("Enter port number: "))
   
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    s.bind((host, port))  
    s.listen(5)  
    m = ""
    client_id = 0

    print("Server listening @ {}:{}".format(host, port))

    while True:
        
        c, addr = s.accept()  
        m = c.recv(1024).decode()

        print("Message from client: " + str(m))

        if m[0] == "/":
            command(checkClients(addr), m)
            c.close()

        elif(m == "server_id"):
            check = checkClients(addr)
            print("Check: " + str(check))
            if(check == False):
                print("First Time Connection from " + str(addr[0]) + " has been established.")
                addClient(c, addr, client_id)
                client_id += 1
                print("Client Added")
            else:
                m = ("$" + str(check.ID)).encode()  
                print("Sending: " + str(m))
                c.send(m)
                c.close()

        else:

            c.send(("Message from server: Received message from client: " + str(m)).encode())
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

    



    