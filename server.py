import socket

def server_program():
    host = 'localhost'
    port = 5000 
    server_socket = socket.socket()

    server_socket.bind((host, port))

    server_socket.listen(1) #number of clients
    conn, address = server_socket.accept() # accept new connection 

    print("connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        #data = input(' -> ')
        #conn.send(data.encode())
        data = 'message received'
        conn.send(data.encode())
    conn.close() #close the connection 

if __name__ == '__main__':
    server_program()