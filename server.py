import socket



def listen(host='127.0.0.1', port=9090):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	s.bind((host, port))
	print(f'Listening at {host}:{port}')

	members = []
	while True:
		msg, addr = s.recvfrom(2048)

		if addr not in members:
			members.append(addr)

		if not msg:
			continue

		client_id = addr[1]
		if msg.decode('ascii') == '__join':
			print(f'Client {client_id} joined chat')
			continue

		msg = f'client{client_id}: {msg.decode("ascii")}'
		for member in members:
			if member == addr:
				continue

			s.sendto(msg.encode('ascii'), member)


if __name__ == '__main__':
	listen()



