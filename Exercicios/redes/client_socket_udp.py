import socket
import sys

rhost = sys.argv[1]
rport = int(sys.argv[2])

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    msg_snd = input("[#]> ")
    s.sendto(msg_snd.encode(),(rhost,rport))
    if msg_snd.strip() == 'exit':
        s.close()
        break
    #dados, addr = s.recvfrom(1024)
    #print(f"{addr} -> {dados.decode()}")