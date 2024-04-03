import socket

port=9090
sock = socket.socket()
sock.bind(('', port))
print("Server is starting")
sock.listen(0)
print("Port",port,"is listing")
#conn, addr = sock.accept()
print("Client is accepted")
# print("Client adress:",addr[0])
# print("Client port:",addr[1])

msg = ''

while True:
	conn, addr = sock.accept()
	print("Client adress:", addr[0])
	print("Client port:", addr[1])
	data = conn.recv(1024)
	if data.decode() == 'exit':
		break
	msg = data.decode()
	conn.send(msg.upper().encode())
	print(msg)
	conn.close()

