
import socket

if __name__ == "__main__":

    port = int(input("Enter port number: ")) 
    num = int(input("Enter host number: "))

    host = "elnux" + num + ".cs.umass.edu"

    s = socket.socket()
    s.connect((host, port))

    message = "Testing Request"
    s.sendall(message.encode()) 

    data = s.recv(1024).decode()
    print(data)
    s.close()