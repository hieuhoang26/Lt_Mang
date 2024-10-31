import socket

if __name__ == '__main__':
    # s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    # s.bind(('127.0.0.1', 9050))
    # try:
    #     s.listen(5)
    #     client_sk, client_addr = s.accept()
    # except s.error as e:
    #     print("fail: ".format(e))
    # print("client addr : {}".format(client_addr))
    # while True:
    #     data = input("enter text")
    #     client_sk.send(data.encode('utf-8'))
    #     data = client_sk.recv(4096)
    #     print("receive from client:")
    #     print(data.decode('utf-8'))
    #     if data.decode('utf-8') == 'bye':
    #         client_sk.send('bye'.encode('utf-8'))
    #         client_sk.close()
    #         break
    #
    # s.close()

    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9050))
    while True:
        try:
            s.listen(5)
            client_sk, client_addr = s.accept()
        except s.error as e:
            print("fail: ".format(e))
    print("client addr : {}".format(client_addr))
    while True:
        data = input("enter text")
        client_sk.send(data.encode('utf-8'))
        data = client_sk.recv(4096)
        print("receive from client:")
        print(data.decode('utf-8'))
        if data.decode('utf-8') == 'bye':
            client_sk.send('bye'.encode('utf-8'))
            client_sk.close()
            break

    s.close()
