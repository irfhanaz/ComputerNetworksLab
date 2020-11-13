import socket
host = socket.gethostname()
port = 6666
buff = 1024

client = socket.socket()
client.connect((host, port))

while True:
    sent_msg = input("Enter File Path: ")
    client.send(sent_msg.encode())
    line_count = -1
    while True:
        receipt_msg = client.recv(buff).decode()

        if not receipt_msg or receipt_msg == "End of File":
            print()
            print(receipt_msg)
            print("Connection Terminated!")
            client.send(("STOP").encode())
            break

        line_count += 1

        if(line_count == 0):
            print(receipt_msg)
            continue

        client_file = open("clientfile.txt", "a+")
        client_file.write(receipt_msg)
        client_file.close()

        print("Line #", line_count, ": ", receipt_msg)

    client.close()
    break
    