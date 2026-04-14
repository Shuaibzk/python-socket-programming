import socket

data = 16
format = "utf-8"
server_port = 4500

hostname = socket.gethostname()
client_ip = socket.gethostbyname(hostname)  # get ip
server_ip = client_ip
server_socket_addr = (server_ip, server_port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_socket_addr)

server.listen()
print("Server is listening...")

while True:
    server_sock, client_addr = server.accept()
    print(f"Conneted to client: {client_addr}")
    connected = True
    while connected:
        length_upcoming = server_sock.recv(data).decode(format)
        print(f"Length of client's message is: {length_upcoming}")
        if length_upcoming:
            message = server_sock.recv(int(length_upcoming)).decode(format)
            
            if message == "disconnect":
                connected = False
                print(f"Connection terminated with: {client_addr}")
                server_sock.send("Byee!!".encode(format))
            else:
                print(f'Message from client is: {message}')
                server_sock.send("Messaag recieved successfully".encode(format))

    server_sock.close()                