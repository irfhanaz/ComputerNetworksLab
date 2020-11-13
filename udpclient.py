import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 6666
while True:
  message = input(">> ")
  client.sendto(message.encode(), (host, port))
  sentence, addr = client.recvfrom(1024)
  print ("Server: ", sentence.decode())
  client.sendto(sentence, (host, port))
  if(sentence == '/EXIT/'):
    break
client.close()