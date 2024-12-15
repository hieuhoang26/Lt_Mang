import socket
HOST = "127.0.0.1"
PORT = 9850

if __name__ == '__main__':
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    s.connect((HOST, PORT))
    while True:
        text = input("Text:")
        s.sendto(text.encode('utf-8'), (HOST, PORT))
        data, addr = s.recvfrom(1024)
        print("Recv from client: {}".format(data.decode('utf-8')))
    s.close()