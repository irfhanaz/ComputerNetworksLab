import socket
client = socket.socket()
host = socket.gethostname()
port = 6666
client.connect((host, port))
client.send(bytes("Katie", 'utf-8'))
while True:
    msg = client.recv(1024)
    if msg == 'quit' or not msg:
        print("*Client Quitting*")
        break
    else:
        print("Server: ", msg.decode())
        msg = input("Client: ")
        client.send(msg.encode())
client.close()
