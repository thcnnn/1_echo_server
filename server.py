import socket
import json
import hashlib
port=9090
sock = socket.socket()
sock.bind(('', port))
print("Server is starting")
sock.listen(1)
print("Port",port,"is listing")
def load_users():
	try:
		with open("users.json", "r") as file:
			return json.load(file)
	except FileNotFoundError:
		return {}
def save_users(user_ip, user_name, user_pass):
	with open("users.json", "r") as file:
		data = json.load(file)
		data[user_ip] = {"name": user_name, "password": user_pass}
		with open("users.json", "w") as outfile:
			json.dump(data, outfile, indent=2)

msg = ''
def handle_client(conn, addr):
	users = load_users()
	client_ip = addr[0]

	if client_ip in users:
		conn.send(f"Добрый день, {users[client_ip]['name']}!\n".encode())
		conn.send("Введите пароль: ".encode())
		password = conn.recv(1024).decode().strip()

		hashed_password = hashlib.sha256(password.encode()).hexdigest()

		if hashed_password == users[client_ip].get("password"):
			conn.send("Аутентификация успешна.".encode())
		else:
			conn.send("Ошибка аутентификации. Неверный пароль.".encode())

	else:
		conn.send("Представьтесь: ".encode())
		name = conn.recv(1024).decode().strip()
		conn.send("Укажите пароль: ".encode())
		password = conn.recv(1024).decode().strip()
		conn.send("Регистрация успешна.".encode())
		hashed_password = hashlib.sha256(password.encode()).hexdigest()

		users[client_ip] = {"name": name, "password": hashed_password}
		save_users(str(client_ip), name, hashed_password)

	conn.close()
while True:
	conn, addr = sock.accept()
	print("Client is accepted")
	print("Client adress:", addr[0])
	print("Client port:", addr[1])
	handle_client(conn, addr)



