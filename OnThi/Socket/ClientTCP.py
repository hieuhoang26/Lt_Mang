import socket

HOST = "127.0.0.1"
POST = 9050

if __name__ == '__main__':
    sk = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
    try:
        sk.connect((HOST,POST))
        while True:
            data = input("input:")
            sk.sendall(data.encode('utf8'))

            if data == 'exit':
                break
            res = sk.recv(1024)
            print("Recv from Ser: {}".format(res.decode('utf-8')))

    except socket.error as e:
        print(f"Socket error: {e}")

    finally:
        sk.close()
        print("Connection closed")