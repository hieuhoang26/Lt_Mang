import socket
if __name__ =='__main__':
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    s.connect(('127.0.0.1',9050))
    while True:
        data = s.recv(4096)
        print("receive from server:")
        print(data.decode('utf-8'))
        if(data.decode('utf-8')=='bye'):
            break
        data = input("enter text:")
        s.send(data.encode('utf-8'))
    s.close()