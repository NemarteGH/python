import os
import socket
import sys

# Adicionando o diretorio acima ao patch para conseguir acessar o modulo ncores.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Modulos.ncores as ncores

bannerkey = 1
banner = f"""{ncores.green}
███╗   ██╗███████╗ █████╗ ███╗   ██╗███╗   ██╗
████╗  ██║██╔════╝██╔══██╗████╗  ██║████╗  ██║
██╔██╗ ██║█████╗  ███████║██╔██╗ ██║██╔██╗ ██║
██║╚██╗██║██╔══╝  ██╔══██║██║╚██╗██║██║╚██╗██║
██║ ╚████║███████╗██║  ██║██║ ╚████║██║ ╚████║
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝            
----------------------------------------------
  [1]Chat  |  [2]Text to Base64  |  [3]Exit
----------------------------------------------
{ncores.reset}"""
banner2 = f"""{ncores.green}----------------------------------------------
  [1]Chat  |  [2]Text to Base64  |  [3]Exit
----------------------------------------------{ncores.reset}"""
dic = {
    "close":"[!]Clossing_Connection[!]",
    "tapenter":f"\n{ncores.red}[!]type [ANY] to back to main menu[!]{ncores.reset}",
    "lines":"------------------------------------",
    "menub64":"======Starting_Base64_function======\n"
              "------------EnterYourText-----------",
    "chatmenu":f"============================\n"
               f"{ncores.red}"
               f"[!] Starting chat...\n"
               f"[!] Type 'exit' to exit\n"
               f"[!] Send a msg and wait!\n"
               f"[!] Server can close chat\n"
               f"{ncores.reset}"
               f"=========Chat_Open=========="
    }

serverinterface = "0.0.0.0" # Setting interface
serverport = int(sys.argv[1]) # Aceita uma porta customizavel lendo o argv
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPV4, TCP.
s.bind((serverinterface,serverport)) # Configurando porta e interface.
s.listen(1) # Coloca o servidor para escutar conforme configurado.
s.settimeout(10) # Determina timeout de conexão, se ninguém se conectar em 10 segundos fecha.
print("Server Running".center(45,'=')) # Mostra mensagem
print(f"{ncores.bold}[#]> Listening for connections on {serverinterface}:{serverport}{ncores.reset}") # Mostra mensagem

try:
    con_obj , client_add  = s.accept() # Ao receber uma conexão, salva o objeto e endereço da conexão em variáveis.
    print(f"[#]> Connection received: {ncores.red}{client_add[0]}:{client_add[1]}{ncores.reset}") # Mostra a conexão

except socket.timeout:
    print("[#]> No connections, clossing socket!\n")
    s.close()
    exit()

def simplechat():
    con_obj.send(dic["chatmenu"].encode())
    print(f'New Chat from {client_add[0]}'.center(45,'='))

    while True:

        reschat = con_obj.recv(1024).decode()
        # Verify if the client wants to close the connection
        if reschat.strip() == "exit" :
            print(45*"=")
            print("[#]> Chat closed by client")
            mainmenu()

        print(f'[cli]>: {reschat}'.strip())
        while True:
            mensagem = input("[#]>: ")
            if mensagem.strip() == '':
                mensagem = input("[#]>: ")
                continue
            else:
                break

        # Verify if server wants to close the connection
        if mensagem.strip() == "exit" :
            con_obj.send("Closed_by_Server".center(28,'=').encode() + dic["tapenter"].encode())
            print(45*"=")
            if con_obj.recv(1024).decode():
                mainmenu()

        else:
            con_obj.send("[srv]>: ".encode() + mensagem.encode())

def texttobase64():
    from base64 import b64encode
    con_obj.send(dic["menub64"].encode())
    text = con_obj.recv(1024).strip()

    if text.decode().strip() == "exit":
        mainmenu()

    else:
        # Não precisou do encode porque a função b64encode já retorna o resultado representado em bytes.
        con_obj.send(dic["lines"].encode() + '\n'.encode() + b64encode(text)
                     + '\n'.encode() + dic["lines"].encode() + dic["tapenter"].encode())
        print(f"[#]> Base64 object sent to client: {ncores.magenta}{b64encode(text)}{ncores.reset}")
        if con_obj.recv(1024).decode():
            mainmenu()

def showbannercomp():
    con_obj.send(banner.encode())

def showbannersmall():
    con_obj.send(banner2.encode())

def mainmenu():
    global bannerkey
    if bannerkey == 1:
        bannerkey = 0
        showbannercomp()
    else:
        showbannersmall()

    while True:
        res = con_obj.recv(1024).decode()

        if res.strip() == '1':
            simplechat()

        elif res.strip() == '2':
            texttobase64()

        elif res.strip() == '3' or res.strip() == 'exit':
            con_obj.send(f"{ncores.red}{dic["close"]}{ncores.reset}".encode())
            print("[#]> Client has been closed connection")
            s.close()
            exit()

        else:
            con_obj.send("[#]> Invalid Choice".encode())
            continue

mainmenu()

