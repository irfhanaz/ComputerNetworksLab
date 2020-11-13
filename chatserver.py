import socket
s = socket.socket()
from threading import Thread
def thread():
	while True:
		msg = conn.recv(1024)
		print("Client Request: " + msg.decode())
		if msg == 'quit' or not msg:
			print("Server Exit....")
			break  
		msg = input("Server Response: ")
		conn.sendall(msg.encode())  
host = socket.gethostname()
port = 6666
s = socket.socket()		
s.bind((host, port))
s.listen(5)
print("Clients may now join. Wait State....")
while True:
	conn, addr = s.accept()	        
	print("Connected by ", addr)
	x = Thread(target=thread)
	x.start()
conn.close()
