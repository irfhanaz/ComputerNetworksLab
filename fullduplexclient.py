import socket
from time import ctime
import threading
host = socket.gethostname()
port = 6666
buff = 1024

client = socket.socket()
client.connect((host, port))

def receive():
    while True:
        receipt_msg = client.recv(buff).decode()
        if not receipt_msg:
            print ("Connection Terminated!")
            break
        print()
        print("<<Server>>:", receipt_msg)

def send():
    while True:
        sent_msg = input(">> ")
        client.send(sent_msg.encode())

conn1 = threading.Thread(target=send, name=1)
conn2 = threading.Thread(target=receive, name=2)

conn1.start()
conn2.start()
