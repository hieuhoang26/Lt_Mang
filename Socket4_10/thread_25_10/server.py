# Tao giao thuc rieng
# 2 client . client 1 dc uu tien truoc
# process -> n thread

import socket
import threading
host = "127.0.0.1"
port = 9050


def create_socket(host, port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind((host, port))
    sk.listen(10)
    return sk

def receive_msg(sk):
    data = bytearray()
    msg = ''
    while not msg:
        b = sk.recv(1024)
        if not b:
            raise ConnectionError()
        data = data + b
        if b'\0' in b:
            msg = data.rstrip(b'\0')
    msg = msg.decode('utf-8')
    return msg


def create_msg(sk, msg):
    msg = msg + '\0'
    return msg.encode('utf-8')


def send_msg(sk, msg):
    data = create_msg(sk, msg)
    sk.sendall(data)


if __name__ == '__main__':
    sk1 = create_socket(host, port)
    addr = sk1.getsockname()
    print('Dia chi cuc bo {}'.format(addr))
    while True:
        client_socket, addrc = sk1.accept()
        print('Dia chi cuc bo {}'.format(addrc))
        try:
            msg = receive_msg(client_socket)
            print('{}:{}'.format(client_socket, msg))
            send_msg(client_socket, msg)
        except ConnectionError:
            print("Loi")
        finally:
            print("Dong connection{}".format(addrc))
            client_socket.close()
