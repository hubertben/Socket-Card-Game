
import tkinter as tk
import socket

port = None
host = None

label = None
server_id = None

def send_message(m):
    
    if m == "quit":
        exit() 

    if m == "":
        return

    s = socket.socket()
    s.connect((host, port))
    s.send(m.encode())

    r = s.recv(1024).decode()

    if r == "kill":
        exit()

    label.config(text=r)
    s.close()

        
def getServerID(host, port):
    
    s = socket.socket()
    print("Connecting to server...")

    s.connect((host, port))
    print("Connected to server!")

    post = "server_id"
    
    s.send(post.encode())
    r = s.recv(1024).decode()
    server_id = int(r[1:])

    print("Server ID: " + str(server_id))
    s.close()
    

if __name__ == "__main__":

    port = int(input("Enter port number: "))

    num = int(input("Enter host number: "))
    host = "elnux" + str(num) + ".cs.umass.edu"
    server_id = -1

    print("Server listening @ {}:{}".format(host, port))
    getServerID(host, port)


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

    
