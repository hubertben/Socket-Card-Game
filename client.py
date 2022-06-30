
import socket

if __name__ == "__main__":

    port = int(input("Enter port number: "))

    if(port < 1024 or port > 65535):
        port = 19487


    num = int(input("Enter host number: "))
    host = "elnux" + str(num) + ".cs.umass.edu"
    server_id = -1
    

    while True:
        s = socket.socket()
        s.connect((host, port))
        
        m = input("Enter message: ")

        s.send(m.encode())

        r = s.recv(1024).decode()
        print("Response:\t", str(r))

        
        if(r[0] == "$"):
            server_id = int(r[1])
            print("Server ID: " + str(server_id))

       
        s.close()

        if(str(m) == "quit"):
            break

        

    