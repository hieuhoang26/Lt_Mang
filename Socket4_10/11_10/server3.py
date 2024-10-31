# client gui ser de nhap file : dir -> gui lai danh sach file . chon file va ghi vao file
import socket
import os

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    s.bind(('127.0.0.1', 9050))
    while True:
        try:
            s.listen(5)
            client_sk, client_addr = s.accept()
        except s.error as e:
            print("Connection fail {}".format(e))
        print("client_address: {}".format(client_addr))
        while True:
            data = input('enter text: ')
            client_sk.send(data.encode("utf-8"))
            data = client_sk.recv(4096)
            print("receive from client: ")
            print(data.decode("utf-8"))
            if (data.decode('utf-8') == 'dir'):
                current_dir = os.getcwd()
                files = os.listdir(current_dir)
                c = ""
                for f in files:
                    c += f
                    c += "\\ \n"
                client_sk.send(c.encode('utf-8'))
            if "." in data.decode('utf-8'):
                with open(data.decode('utf-8'), 'r', encoding='utf-8') as f:
                    d = f.read()
                client_sk.send(d.encode('utf-8'))

            if (data.decode("utf-8") == "bye"):
                client_sk.send("bye".encode("utf-8"))
                client_sk.close()
                break
    s.close()