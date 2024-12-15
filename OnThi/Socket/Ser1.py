# Xây dựng chương trình theo mô hình Client-Server sử dụng socket theo giao thức TCP
# a. Client: gửi tín hiệu kết nối đến server
# Cho phép người dùng nhập 1 chuỗi ký tự từ bản phim
# Gửi chuỗi đã nhập đến server
# Nhận kết quả trả về

# b. Server: Chấp nhận kết nối
# Nhận kết nối từ client, hiển thị thông tin client
# Nhận xâu ký tự tử client
# Đếm số ký tự in hoa trong chuỗi
# Trả kết quả về cho client

import socket
HOST = "127.0.0.1"
PORT = 9850

if __name__ == '__main__':
    s = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    try:
        s.listen(5)
        print("Ser is listening...")
        while True:
            client_sk, client_addr = s.accept();
            print("Client info: ",client_addr)

            while True:
                recv = client_sk.recv(1024).decode('utf-8')
                print("Recv from client: {}".format(recv))
                if recv == 'exit':
                    break
                # Check Upcase
                if recv.startswith("UP "):
                    str_to_check = recv.split()[1]
                    data = sum(1 for i in str_to_check if i.isupper())
                    client_sk.send(str(data).encode('utf-8'))
    except s.error as e:
        print("error: {}".format(e))
    finally:
        s.close()