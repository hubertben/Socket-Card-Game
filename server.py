
import socket

if __name__ == "__main__":
    
    port = int(input("Enter port number: ")) # Used While Testing: 19487
   
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname() # Get local machine name
    s.bind((host, port))  # Bind to the port

    s.listen(5)  # Now wait for client connection
    print("Server listening @ {}:{}".format(host, port))
    while True:
        c, addr = s.accept()  # Establish connection with client
        print(f"Connection from {addr} has been established.")
        m = c.recv(1024).decode() # Get the message
        
        print("Request:\t", m)

        s = "Testing"

        c.send(s.encode())  # Send the response
        
        c.close()  # Close the connection
        