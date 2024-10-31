import socket

host = "127.0.0.1"
port = 9050

def create_msg(msg):
    msg = msg + '\0'
    return msg.encode('utf-8')

def receive_msg(sk):
    data = bytearray()
    msg = ''
    while not msg:
        b = sk.recv(1024)
        if not b:
            raise ConnectionError()
        data = data + b
        if b'\0' in b:
            msg = data.rstrip(b'\0')
    msg = msg.decode('utf-8')
    return msg

def send_msg(sk, msg):
    data = create_msg(msg)
    sk.sendall(data)

if __name__ == '__main__':
    while True:
        try:
            sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sk.connect((host, port))
            message = input("Nhap tin nhan muon gui: ")
            if message == 'exit':
                break
            send_msg(sk, message)
            print("Cho phan hoi tu server...")
            response = receive_msg(sk)
            print(f"Server phan hoi: {response}")
        except ConnectionError:
            print("Mat ket noi voi server")
        finally:
            print("Dong ket noi")
            sk.close()
