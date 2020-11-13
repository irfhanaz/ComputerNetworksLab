import socket
s = socket.socket()
print("Successful Socket Creation")
host = socket.gethostname()
port = 6666
s.bind((host, port))
s.listen(14)
print("Wait State...")
connection_socket, address = s.accept()
while True:
  sentence = connection_socket.recv(1024).decode()
  print('Client: ', sentence)
  message = input(">> ")
  connection_socket.send(message.encode())
  if(message == '/EXIT/'):
    connection_socket.close()
    break
    
