
import socket

if __name__ == "__main__":
    
    port = int(input("Enter port number: "))
   
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname() 
    s.bind((host, port))  
    s.listen(5)  
    print("Server listening @ {}:{}".format(host, port))
    
    while True:
        c, addr = s.accept()  
        print("Connection from " + addr + " has been established.")
        m = c.recv(1024).decode() 
        
        print("Request:\t", m)

        s = "Testing"

        c.send(s.encode())
        
        c.close() 
        