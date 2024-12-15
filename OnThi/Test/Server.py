import socket

HOST = "127.0.0.1"
PORT = 9050

if __name__ == '__main__':
    # s = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    try:
        s.bind((HOST, PORT))
        # s.listen(5)
        print("Ser is listening")
        while True:
            #     client_sk, client_addr = s.accept()
            #     print(f"Client connected from {client_addr}")
            #
            #     while True:
            #         data = client_sk.recv(1024).decode('utf-8')
            #         print("Rec from client: {}".format(data))
            #
            #         dt = input("text:")
            #         client_sk.send(data.encode('utf-8'))
            data, addr = s.recvfrom(1024)
            print("Rec from client: {}".format(data))
            dt = input("text:")
            s.send(data)
    except s.error as e:
        print("Errror: {}".format(e))
    finally:
        s.close()
