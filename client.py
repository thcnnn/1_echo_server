import socket
from time import sleep
port = input('port no: ')
try:
    port = int(port)
except ValueError:
    print("Invalid port number. Using default port 9090.")
    port = 9090
host_name = input('host_name: ') or 'vboxuser'
sock = socket.socket()
sock.setblocking(1)
sock.connect(('', 9090))

msg = input("Your string: ")
#msg = "Hi!"
sock.send(msg.encode())

data = sock.recv(1024)
sock.close()
print(data.decode())