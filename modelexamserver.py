import socket
s = socket.socket()
host = socket.gethostname()
port = 6666
s.bind((host, port))
s.listen(5)
print("Passive Open Established. Waiting for a connection.....")
c, addr = s.accept()
print("Connection Successfully Established")

while True:
    file_name = c.recv(1024).decode()
    if not file_name or file_name == "STOP":
        print("Connection Terminated by Client\n")
        break
    print("File Name Received: ", file_name)
    with open(file_name, "r") as fp:
        msg = "File Contents: "
        c.send(msg.encode())
        for line in fp:
            c.send(line.encode())
            continue
        print()
        break
    msg = "EOF"
    c.send(msg.encode())

c.close()



