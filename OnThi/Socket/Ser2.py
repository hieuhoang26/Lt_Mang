# Tìm min max 2 số UDP

import socket
HOST = "127.0.0.1"
PORT = 9850

if __name__ == '__main__':
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    s.bind((HOST, PORT))
    while True:
        data, addr = s.recvfrom(1024)
        print("Recv from client: {}".format(data.decode('utf-8')))
        if data == 'exit':
            break
        dt = data.decode('utf-8')
        if dt.startswith('min '):
            a = data.split()[1]
            b = data.split()[2]
            text = a if a < b  else b
            s.sendto(str(text).encode('utf-8'),addr)
    s.close()