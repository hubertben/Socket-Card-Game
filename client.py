
import socket

if __name__ == "__main__":

    port = int(input("Enter port number: "))

    if(port < 1024 or port > 65535):
        port = 19487


    num = int(input("Enter host number: "))

    host = "elnux" + str(num) + ".cs.umass.edu"

    

    while True:
        s = socket.socket()
        s.connect((host, port))
        
        m = input("Enter message: ")

        s.send(m.encode())

        r = s.recv(1024).decode()
        print("Response:\t", str(r))

        s.close()

        if(str(m) == "quit"):
            break

        

    