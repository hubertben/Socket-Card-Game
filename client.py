
import socket

if __name__ == "__main__":

    port = 19487 #int(input("Enter port number: ")) 
    num = int(input("Enter host number: "))

    host = "elnux" + str(num) + ".cs.umass.edu"

    s = socket.socket()
    s.connect((host, port))

    message = "get"
    s.sendall(message.encode()) 
    data = s.recv(1024).decode()


    message = "quit"
    s.sendall(message.encode()) 
    data = s.recv(1024).decode()

    print(data)
    s.close()