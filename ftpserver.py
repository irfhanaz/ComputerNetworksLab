import socket
buff = 1024
server = socket.socket()
host = socket.gethostname()
port = 6666
server.bind((host, port))
server.listen(5)
print("Waiting for a connection...")
client, addr = server.accept()
print("Connection Successfully Established!")

while True:
    receipt_msg = client.recv(buff).decode()
    if not receipt_msg or receipt_msg == "STOP":
        print("Connection Terminated!")
        break
    print()
    print("File Path: ", receipt_msg)

    with open(receipt_msg, "r") as fp:
        msg = "File Contents: "
        client.send(msg.encode())
        for line in fp:
            client.send(line.encode())
            continue
        break
    
    print()
    msg = "End of File"
    client.send(msg.encode())
        
client.close()

