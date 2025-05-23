import socket
import sys

lhost = "0.0.0.0"
lport = int(sys.argv[1])

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((lhost,lport))
print (f"UDP server listening on {lhost}:{lport}")

while True:
    data, addr = s.recvfrom(1024)
    print(f"[#]> {data.decode()}")
    if data.decode().strip() == 'exit':
        s.close()
        break
    #msg = input("[#]> ")
    #s.sendto(msg.encode(),addr)
