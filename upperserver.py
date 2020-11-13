import socket
s = socket.socket()
print("Successful Creation of Socket")
host = socket.gethostname()
port = 6666
s.bind((host,port))
s.listen(11)
print("Wait State.....")
while True:
    conn,addr = s.accept()
    print("Successful connection with Client: ",addr)
    msg = conn.recv(1024).decode()
    conn.send(bytes(msg.upper(),'utf-8'))
    conn.close()
