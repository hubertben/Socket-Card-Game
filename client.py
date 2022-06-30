
import socket

if __name__ == "__main__":

    port = 19487 #int(input("Enter port number: ")) 
    num = int(input("Enter host number: "))

    host = "elnux" + str(num) + ".cs.umass.edu"

    s = socket.socket()
    s.connect((host, port))

    while True:
        m = input("Enter message: ")
        s.send(m.encode())
        
        if(m == "quit"):
            break
        
        r = s.recv(1024).decode()
        print("Response:\t", str(r))

    s.close()