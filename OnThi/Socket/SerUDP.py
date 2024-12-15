import socket
HOST = "127.0.0.1"
POST = 9050
if __name__ == '__main__':
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    s.bind((HOST,POST))
    data, addr = s.recvfrom(1024)
    print("Client gui {}".format(data))
    data = 'hello client'
    s.sendto(data.encode('utf-8'), addr)
    s.close()
