import socket
import threading
def receive(client, nickname):
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            if message == 'NICK':
                client.send(nickname.encode("ascii"))
            else:
                print(message)
        except:
            print("ERROR: Something went wrong... Closing the client!")
            client.close()
            break

def write(client, nickname):
    while True:
        message = f"{nickname}: {input('')}"
        try:
            client.send(message.encode("ascii"))
        except OSError:
            print("ERROR: You failed to send the message to the server! Closing the client!")
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("CLIENT: Please enter a proper port number...")
    port = int(input())
    address = input()
    try:
        nickname = input("CLIENT: Please enter your nickname...")
        client.connect((address, port))
        receive_thread = threading.Thread(target=receive, args=(client, nickname,))
        receive_thread.start()

        write_thread = threading.Thread(target=write, args=(client, nickname,))
        write_thread.start()
    except:
        print("ERROR: Couldn't find server... Closing client!")
        client.close()

main()