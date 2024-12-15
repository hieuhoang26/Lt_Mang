import socket

HOST = "127.0.0.1"
PORT = 9050

if __name__ == '__main__':
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    try:
        s.connect((HOST,PORT))
        while True:
            data = input("text:")
        #     s.send(data.encode('utf-8'))
            s.sendto(data.encode('utf-8'),(HOST,PORT))
        #
            dt = s.recvfrom(1024)
            print("Rec from client: {}".format(dt))

    except s.error as e:
        print("Errror: {}".format(e))
    finally:
        s.close()