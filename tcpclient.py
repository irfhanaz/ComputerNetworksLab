import socket
client = socket.socket()
host = socket.gethostname()
port = 6666
client.connect((host, port))
while True:
  sentence = input(">> ")
  client.send(sentence.encode())
  if(sentence == '/EXIT/'):
    client.close()
    break
  message = client.recv(1024)
  print ("Server: ", message.decode())
  