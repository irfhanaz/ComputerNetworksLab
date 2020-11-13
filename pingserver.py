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
    print("Successful Connection with Client: ", addr)
    clmsg = conn.recv(1024).decode()
    if(clmsg == 'PING' or clmsg == 'ping'):
        msg = 'SERVER: PONG'
    else:
        msg = 'SERVER DROPPED'
    conn.send(bytes(msg,'utf-8'))
    conn.close()
