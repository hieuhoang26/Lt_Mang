# import socket
# if __name__ =='__main__':
#     s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
#     s.connect(('127.0.0.1',9050))
#     while True:
#         data = input("enter text:")
#         s.send(data.encode('utf-8'))
#         data = s.recv(4096)
#         print("receive from server:")
#         print(data.decode('utf-8'))
#
#     s.close()
import socket

if __name__ == '__main__':
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 9050))

    while True:
        data = input("Enter text (type 'exit' to quit): ")
        s.send(data.encode('utf-8'))

        if data == 'exit':
            break

        response = s.recv(4096)
        print("Received from server:", response.decode('utf-8'))

    s.close()
