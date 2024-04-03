import socket
from datetime import datetime
port=input('port no: ')
try:
    port = int(port)
except ValueError:
    print("Invalid port number. Using default port 9090.")
    port = 9090
sock = socket.socket()
sock.bind(('', port))
with open('logs', 'a') as file:
	file.write(("Server is starting | " + str(datetime.now())))
	file.write('\n')
sock.listen(1)
with open('logs', 'a') as file:
	file.write(("Port" + str(port) + "is listing | " + str(datetime.now())))
	file.write('\n')
	file.write(("Client is accepted | "+ str(datetime.now())))
	file.write('\n')
#print(socket.gethostname())
msg = ''

while True:
	conn, addr = sock.accept()
	with open('logs', 'a') as file:
		file.write(("Client adress:" + (addr[0]) + ' | ' + str(datetime.now())))
		file.write('\n')
		file.write(("Client port:" + str(addr[1]) + '| ' + str(datetime.now())))
		file.write('\n')
	data = conn.recv(1024)
	if data.decode() == 'exit':
		break
	msg = data.decode()
	conn.send(msg.upper().encode())
	print(msg)
	conn.close()



