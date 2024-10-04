import socket
if __name__ =='__main__':
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    s.connect(('127.0.0.1',9050))
    data = s.recv(4096)
    print("receive from server:")
    print(data.decode('utf-8'))
    data = "hello server"
    s.send(data.encode('utf-8'))
    s.close()