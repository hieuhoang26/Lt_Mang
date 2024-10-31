# ser kiem tra neu la GET TIME lay thoi gian hien tai va gui ve
# use TCP

import socket
from time import ctime

if __name__ == '__main__':
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9050))
    s.listen(5)
    print("Server is listening...")
    while True:
        try:
            client_sk, client_addr = s.accept()
            print(f"Client connected from {client_addr}")

            data = client_sk.recv(4096)
            print("Received from client:", data.decode('utf-8'))

            if data.decode('utf-8') == 'GET TIME':
                client_sk.send(bytes(ctime(), 'utf-8'))
            else:
                client_sk.send(b"Unknown command")

            client_sk.close()

        except socket.error as e:
            print(f"Error: {e}")
    s.close()
