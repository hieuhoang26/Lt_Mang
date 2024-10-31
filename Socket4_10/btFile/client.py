import socket
import os
host = "127.0.0.1"
port = 9095
DOWNLOAD_DIR = "D:\\LtMang\\testFile\\download"

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,port))
    while True:
        print(s.recv(1024).decode(), end="")
        username = input()
        s.send(username.encode())

        print(s.recv(1024).decode(), end="")
        password = input()
        s.send(password.encode())

        response = s.recv(1024).decode()
        print(response)
        if "401" in response:
            print("Login Failed - Unauthorized")
        if "200" in response:
            print("Login Sucess!")
            break
    try:
        while True:
            command = input("Enter text (or type 'exit' to disconnect): ")
            s.send(command.encode("utf-8"))
            if command.startswith("upload "):
                filedir = command.split()[1]
                if os.path.exists(filedir):
                    try:
                        with open(filedir, "rb") as src:
                            data = src.read(1024)
                            while data:
                                s.sendall(data)
                                data = src.read(1024)
                        print(s.recv(1024).decode("utf-8"))
                    except OSError as err:
                        print("Error:", err)

            elif command.startswith("download "):
                parts = command.split()
                # not have target
                if len(parts) < 3:
                    fileSrc = parts[1]
                    fileTarget = os.path.basename(fileSrc)
                else:
                    fileSrc = parts[1]
                    fileTarget = parts[2]
                    if os.path.isdir(fileTarget):
                        fileTarget=os.path.join(fileTarget,os.path.basename(fileSrc))
                try:
                    with open(fileTarget, "wb") as target:
                        data = s.recv(1024)
                        while data:
                            target.write(data)
                            if len(data) < 1024:
                                break
                            data = s.recv(1024)
                    print(s.recv(1024).decode("utf-8"))
                except OSError as err:
                    print("Error:", err)
            elif command.startswith("ls "):
                print(s.recv(1024).decode("utf-8"))
            elif command.startswith("log "):
                print(s.recv(1024).decode("utf-8"))

            # elif res == 'exit':
            elif command == "exit":
                print("Disconnect server")
                break
            # res = s.recv(1024).decode("utf-8")
            # print("Response from server:", res)
    except socket.error as err:
        print("Error: ", err)
    finally:
        s.close()