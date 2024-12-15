import socket
HOST = "127.0.0.1"
PORT = 9850

if __name__ == '__main__':
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    try:
        s.connect((HOST,PORT))
        while True:
            data = input(f"Text:")
            s.send(data.encode('utf-8'))
            if data == 'exit':
                break
            recv = s.recv(1024).decode('utf-8')
            print("Recv from client: {}".format(recv))
    except s.error as e:
        print("error: {}".format(e))
    finally:
        s.close()