import socket
host = socket.gethostname()
port = 6666

c = socket.socket()
c.connect((host, port))

while True:
    file_name = input("Enter File Path: ")
    c.send(file_name.encode())
    line_count = -1
    while True:
        file_contents = c.recv(1024).decode()

        if not file_contents or file_contents == "EOF":
            print()
            print(file_contents)
            print("Connection Termination Initiated!")
            c.send(("STOP").encode())
            break

        line_count += 1

        if(line_count == 0):
            print(file_contents)
            continue

        client_file = open("clientfile.txt", "a+")
        client_file.write(file_contents)
        client_file.close()

        print("Line #", line_count, ": ", file_contents)

    c.close()
    break
    