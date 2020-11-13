#date time server
import socket
import time
s = socket.socket()
print("Successful Socket Creation")
host = socket.gethostname()
port = 6666
s.bind((host, port))
s.listen(14)
print("Wait State...")
while True:
  connection_socket, address = s.accept()
  print("Connection Successful")
  date = time.strftime("%c")
  message = str(date)
  connection_socket.send(message.encode())
  connection_socket.close()

    