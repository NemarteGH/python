import socket
import sys

rhost = sys.argv[1]
rport = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((rhost,rport))

while True:
    received_msg = s.recv(1024).decode()
    print(f"[#]> {received_msg}")
    send_msg = input("[#]>")
    s.send(send_msg.encode())

    if send_msg.strip() == 'exit':
        s.close()
        exit()

