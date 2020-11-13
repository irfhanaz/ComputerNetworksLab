import threading
import socket
buff = 1024
server = socket.socket()
host = socket.gethostname()
port = 6666
server.bind((host,port))
server.listen(5)

print("Waiting for a connection...")
client, addr = server.accept()
print("Connection Successfully Established!")

def receive():
    while True:
        receipt_msg = client.recv(buff).decode()
        if not receipt_msg:
            print ("Connection Terminated")
            break
        print()
        print("<<Client>>: ", receipt_msg)
def send():
    while True:
        sent_msg = input(">> ")
        if not sent_msg:
            break
        client.send(sent_msg.encode())

conn3 = threading.Thread(target=send, name=3)
conn4 = threading.Thread(target=receive, name=4)

conn3.start()
conn4.start()
