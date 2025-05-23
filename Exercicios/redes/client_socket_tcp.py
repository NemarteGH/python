import socket
import sys

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
rhost = sys.argv[1]
rport = int(sys.argv[2])
s.connect((rhost,rport))

while True:
    msg_rcvd = s.recv(1024).decode()
    print(f'{msg_rcvd}')

    if "[!]Clossing_Connection[!]" in msg_rcvd.strip():
        s.close()
        exit()

    while True:
        msg_snd = input("[#]> ")
        if msg_snd.strip() == '':
            continue
        else:
            s.send(msg_snd.encode())
            break

