import socket
import threading

def broadcast(message, clients):
    for client in clients:
        client.send(message)

def handle(client, clients, nicknames):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} has left the chat!".encode("ascii"))
            nicknames.remove(nickname)
            break

def receive(server, clients, nicknames):
    while True:
        client, address = server.accept()
        print(f"SERVER: Connection with {str(address)} has been established!")

        client.send("NICK".encode("ascii"))
        nickname = client.recv(1024).encode("ascii")
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}!")
        broadcast(f"Welcome to the chat server, {nickname}!".encode("ascii"))
        client.send("Connected to the server!".encode("ascii"))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


def main():
    """
    DESCRIPTION: The main function that operates the TCP server
    :return:
    """
    print("SERVER: Please input any port number between 0 to 65535.")
    port = int(input())
    while (port < 0 or port > 65535):
        print("SERVER: Please input a valid number")
        port = int(input())
    print("SERVER: Initializing server... Please wait...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', port))
    server.listen()
    clients = []
    nicknames = []
    print("SERVER: Listening...")
    receive(server, clients, nicknames)

main()
