import socket
import threading

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



def client_handler(server_sock, client_addr):
    connected = True
    while connected:
        length_upcoming = server_sock.recv(data).decode(format)

        if length_upcoming:
            message = server_sock.recv(int(length_upcoming)).decode(format)
            
            if message == "disconnect":
                connected = False
                print(f"Connection terminated with: {client_addr}")
                server_sock.send("Byee!!".encode(format))
            else:
                print(f"Message from client is: {message}")
                count = 0
                vowels = "aeiou"

                for ch in message.lower():
                    if ch in vowels:
                        count += 1

                if count == 0:
                    reply = "Not enough vowels"
                elif count <= 2:
                    reply = "Enough vowels I guess"
                else:
                    reply = "Too many vowels"

                server_sock.send(reply.encode(format))

    server_sock.close()



while True:
    server_sock, client_addr = server.accept()
    # print(f"Conneted to client: {client_addr}")
    thread = threading.Thread(target=client_handler, args=(server_sock, client_addr))
    thread.start()
                