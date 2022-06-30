
import tkinter as tk
import socket

port = None
host = None

label = None
server_id = None

def send_message(m):

    if m == "":
        return

    s = socket.socket()
    s.connect((host, port))
    s.send(m.encode())
    r = s.recv(1024).decode()

    label.config(text=r)
    
    s.close()

        
def getServerID():
    s = socket.socket()
    s.connect((host, port))
    m = "server_id"
    s.send(m.encode())
    r = s.recv(1024).decode()
    server_id = int(r[1])
    print("Server ID: " + str(server_id))
    s.close()
    

if __name__ == "__main__":

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


    port = int(input("Enter port number: "))

    if(port < 1024 or port > 65535):
        port = 19487


    num = int(input("Enter host number: "))
    host = "elnux" + str(num) + ".cs.umass.edu"
    server_id = -1

    getServerID()

    kinter.mainloop()

    





    

        

        
        

        
        

       
        
        

    