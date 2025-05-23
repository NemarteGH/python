import socket
import sys

lhost = '0.0.0.0'
lport = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((lhost,lport))
s.listen(1)
print("Servidor TCP iniciado!")
conn, conn_addr = s.accept()
conn.send("Bem vindo ao servidor TCP!".encode())
print(f"Conexão recebida de {conn_addr[0]}:{conn_addr[1]}")

while True:
    response = conn.recv(1024).decode()
    print(f"[#]> {response}")
    if response.strip() == 'exit':
        s.close()
        exit()

    sendmsg = input("[#]> ")
    conn.send(sendmsg.encode())
