import socket, sys

helpbanner ="""┌──────────────────────────────────────────────────┐
│ Command syntax: s.py [arg] [value]        │
│══════════════════════════════════════════════════│
│ -lh [host]: Specifies the interface you want to  │
│             use to listen for connections.       │
│ -lp [port]: Specifies the network port you want  │
│             to use to listen for connections.    │
│ -lt [sec]:  Specifies the listening duration.    │
│ -tcp: Creates a TCP server.                      │
│ -udp: Creates a UDP server.                      │
│══════════════════════════════════════════════════│
│If no arguments are given, the default option is: │
│  [0.0.0.0:8080 tcp] - No timeout                 │
│▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│                       
│Command example: s.py -lp 5050 -tcp -lt 50 │
└──────────────────────────────────────────────────┘
"""

class Nserver:

    def __init__(self,protocol='tcp',lhost='0.0.0.0',lport=8080, timeouts=None):

        self.protocol = protocol
        self.lhost = lhost
        self.lport = lport
        self.timeouts = timeouts

        print(f"Current socket settings: {self.protocol}|{self.lhost}:{self.lport}|{self.timeouts}")

    def startserver(self):

        if self.protocol == 'tcp':

            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.bind((self.lhost,self.lport))
            s.settimeout(self.timeouts)
            s.listen(1)
            print(f"TCP server listening on: {self.lhost}:{self.lport}...")

            try:
                conn, addr = s.accept()
                print(f"Connection received from: {addr[0]}:{addr[1]}")

            except TimeoutError:
                print(f"[#]> Listening timeout has been reached. Current Timeout: {self.timeouts}s")
                s.close()
                exit()

            filename = conn.recv(1024).decode().strip()
            filelength = int(conn.recv(1024).decode().strip())

            with open(filename,'wb') as file:
                received_bytes = 0
                while received_bytes < filelength:
                    msg = conn.recv(1024)
                    if not msg:
                        break
                    file.write(msg)
                    received_bytes += len(msg)




        elif self.protocol == 'udp':
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.bind((self.lhost, self.lport))
            s.settimeout(self.timeouts)
            print(f"UDP server listening on {self.lhost}:{self.lport}...")

            try:

                while True:
                    msg_udp, addr = s.recvfrom(1024)
                    print(f"[#]> {msg_udp.decode()}",end='')
                    if msg_udp.decode().strip() == 'exit':
                        s.close()
                        exit()

            except TimeoutError:
                print(f"[#]> Listening timeout has been reached. Current Timeout: {self.timeouts}s")
                s.close()
                exit()

if __name__ == '__main__':

    e_lport = None
    e_lhost = None
    e_protocol = None
    args = {}

    if len(sys.argv[1:]) != 0:

        if any(e in ['-lp', '-lh', '-tcp', '-udp', '--help', '-lt'] for e in sys.argv[1:]):

            try:
                for i in sys.argv:

                    if i == '-lh':
                        args['lhost'] = sys.argv[sys.argv.index('-lh')+1]

                    elif i == '-lp':
                        args['lport'] = int(sys.argv[sys.argv.index('-lp')+1])

                    elif i == '-lt':
                        args['timeouts'] = sys.argv[sys.argv.index('-lt')+1]

                    elif i == '-tcp' or i == '-udp':
                        args['protocol'] = i.strip("-")

                    elif i == '--help':
                        print(helpbanner)
                        exit()

                myclassobject = Nserver(**args)
                myclassobject.startserver()

            except IndexError:
                print("[#]> Argument Error: check lhost, lport and protocol options! Use --help to see the options.")
                exit()
        else:
            print("[#]> Invalid argument. Use --help to see the options.")
    else:
        myclassobject = Nserver()
        myclassobject.startserver()


