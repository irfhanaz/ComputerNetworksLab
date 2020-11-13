#date time client
import socket
client = socket.socket()
host = socket.gethostname()
port = 6666
client.connect((host, port))
message = client.recv(1024)
print ("Current Time: ", message.decode())
client.close()