import socket

HOST = "127.0.0.1"
POST = 9050
if __name__ == '__main__':
    sk = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
    try:
        sk.bind((HOST,POST))
        sk.listen(5)
        print("Ser is listening")
        while True:
            client_sk, client_addr = sk.accept()
            print(f"Client connected from {client_addr}")

            while True:
                data = client_sk.recv(1024).decode("utf-8")
                print("Recv from client: {}".format(data))
                if data == 'exit':
                    client_sk.close()
                    break
                dt = input("input:")
                client_sk.send(dt.encode('utf8'))
    except socket.error as e:
        print(f"Socket error: {e}")
    finally:
        sk.close()
        print("Server stopped")

