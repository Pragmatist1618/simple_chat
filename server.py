import socket


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    host_name = socket.gethostname()
    s_ip = socket.gethostbyname(host_name)

    sock.bind((s_ip, 5050))

    client = []  # Массив где храним адреса клиентов
    print('Start Server')

    while 1:
        data, address = sock.recvfrom(1024)
        print(address[0], address[1], data.decode('utf-8'))

        if address not in client:
            client.append(address)  # Если такого клиента нету , то добавить

        for clients in client:
            if clients == address:
                continue  # Не отправлять данные клиенту, который их прислал
            sock.sendto(data, clients)
