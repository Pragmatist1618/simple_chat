import socket
import threading

key = 567


def crypt_msg(msg):
    crypt = ''

    for i in msg:
        crypt += chr(ord(i) ^ key)

    return crypt


def read_sok():
    while 1:
        data = soc.recv(1024)
        msg = data.decode('utf-8')

        msg = msg.split(']')
        if len(msg) > 1:
            name = msg[0] + ']'

            msg = crypt_msg(msg[1])

            print(name + ' ' + msg)
        else:
            print(msg[0])


if __name__ == '__main__':
    # get ip localhost
    host_name = socket.gethostname()
    s_ip = socket.gethostbyname(host_name)

    # using ip localhost
    server = (s_ip, 5050)  # Данные сервера

    alias = input('Input your name: ')  # Вводим наш псевдоним

    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.bind(('', 0))  # Задаем сокет как клиент
    soc.sendto((alias + ' Connect to server').encode('utf-8'), server)  # Уведомляем сервер о подключении

    thread = threading.Thread(target=read_sok)
    thread.start()

    while 1:
        # get msg
        message = input()
        # шифруем сообщение
        message = crypt_msg(message)
        soc.sendto(('[' + alias + ']' + message).encode('utf-8'), server)
