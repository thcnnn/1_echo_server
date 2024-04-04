import socket
from time import sleep
port = 9090
sock = socket.socket()
#sock.setblocking(0)
sock.connect(('127.0.0.1', 9090))

response = sock.recv(1024).decode()
print(response)

while True:
    data = input()
    sock.send(data.encode())
    response = sock.recv(1024).decode()
    print(response)

    if response == "Представьтесь.":
        name = input("Введите ваше имя: ")
        sock.send(name.encode())
    elif response == "Укажите пароль.":
        print(response == "Укажите пароль.")
        password = input("Введите пароль: ")
        sock.send(password.encode())
    elif response == "Аутентификация успешна." or response == "Регистрация успешна." or "Ошибка аутентификации. Неверный пароль.":
        break

sock.close()