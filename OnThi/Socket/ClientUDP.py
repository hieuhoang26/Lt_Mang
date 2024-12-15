import socket
HOST = "127.0.0.1"
POST = 9050

if __name__ == '__main__':
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    s.sendto("hello ser".encode("utf-8"),(HOST,POST))
    data = s.recvfrom(1024)
    print("Ser gui {}".format(data))
    s.close()