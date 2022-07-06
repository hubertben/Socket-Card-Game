
import tkinter as tk
import socket

port = None
host = None

label = None
server_id = None

s = None

def send_message(m):

    if m == "":
        return

    s.send(m.encode())
    r = s.recv(1024).decode()

    label.config(text=r)
    print("[LOG]:", r)

    if m == "quit":
        exit() 
    
    
    

        


    

if __name__ == "__main__":

    port = int(input("Enter port number: "))

    num = int(input("Enter host number: "))
    host = "elnux" + str(num) + ".cs.umass.edu"
    server_id = -1

    s = socket.socket()
    s.connect((host, port))

    print("Server listening @ {}:{}".format(host, port))


    kinter = tk.Tk()
    kinter.title("Client")
    kinter.geometry("800x300")
    kinter.resizable(False, False)
    kinter.configure(background="gray")

    # add text input field to the window
    text_input = tk.Entry(kinter, width=30)
    text_input.place(x=50, y=50)

    # add button to the window
    button = tk.Button(kinter, text="Send", width=10, command=lambda: send_message(text_input.get()))
    button.place(x=50, y=100)

    label = tk.Label(kinter, text="", width=50)
    label.place(x=50, y=200)


    kinter.mainloop()
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