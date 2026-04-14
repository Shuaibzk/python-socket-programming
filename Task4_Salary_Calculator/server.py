import socket

data = 16
format = "utf-8"
server_port = 4500

hostname = socket.gethostname()
client_ip = socket.gethostbyname(hostname)
server_ip = client_ip
server_socket_addr = (server_ip, server_port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_socket_addr)

server.listen()
print("Server is listening...")

while True:
    server_sock, client_addr = server.accept()
    print(f"Connected to client: {client_addr}")
    connected = True

    while connected:
        length_upcoming = server_sock.recv(data).decode(format)

        if length_upcoming:
            print(f"Length of client's message is: {length_upcoming}")
            message = server_sock.recv(int(length_upcoming)).decode(format)

            if message == "disconnect":
                connected = False
                print(f"Connection terminated with: {client_addr}")
                server_sock.send("Byee!!".encode(format))

            else:
                print(f"Client sent hour: {message}")
                hour = int(message)

                if hour <= 40:
                    salary = hour * 200
                else:
                    salary = 8000 + (hour - 40) * 300

                server_sock.send(f"Salary = Tk {salary}".encode(format))

    server_sock.close()