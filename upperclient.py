import socket
client = socket.socket()
host = socket.gethostname()
port = 6666
client.connect((host,port))
msg = input("Enter the message:")
client.send(bytes(msg,'utf-8'))
Msg = client.recv(1024).decode()
print("Uppercase output: ", Msg)
