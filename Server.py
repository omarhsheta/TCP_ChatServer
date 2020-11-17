import socket

def server_init(port_number, hostname):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((hostname, port_number))
    server.listen()

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
            broadcast(f'{nickname} has left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break

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
    server_init(port, '127.0.0.1')
    clients = []
    nicknames = []
    return None
