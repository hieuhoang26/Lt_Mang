import ftplib
from datetime import datetime
import socket
import os
import threading
import time

USER_DB = "D:\\LtMang\\testFile\\pass.txt"
FILE_DIR = "D:\\LtMang\\testFile\\data"
host = "127.0.0.1"
port = 9095




def handleLogin(client_socket):

    print("Connect Client: ", client_address)
    client_socket.send("Enter username:".encode("utf-8"))
    username = client_socket.recv(1024).decode("utf-8").strip()
    client_socket.send("Enter password:".encode("utf-8"))
    password = client_socket.recv(1024).decode("utf-8").strip()
    return username, password


def handleUpload(client_socket, filedir, username,ftp):
    if os.path.exists(filedir):
        filename = os.path.basename(filedir)
        print("{} is uploading.....".format(filename))
        # filepath = os.path.join(FILE_DIR,filename)
        try:
            with open(f"{filedir}", "wb") as fp:
                data = client_socket.recv(1024)
                while data:
                    fp.write(data)
                    if len(data) < 1024:
                        break
                    data = client_socket.recv(1024)
                response = ftp.storbinary("STOR " + filename, fp)
            print(f"Server response: {response}")
            if not response.startwith("226"):
                print("Upload failed !")
                client_socket.send("Upload file failed !".encode("utf-8"))
            else:
                print(f"Upload file {filedir} completed successfully")
                client_socket.send("Upload file sucess".encode("utf-8"))
        except OSError as err:
            print("Error opening file:", err)
    else:
        print("Source file does not exist.")


# def handleDownload(client_socket, username, fileSrc,fileTarget,ftp):
#     filepath = os.path.join(FILE_DIR, fileSrc)
#     filename = os.path.basename(fileSrc)
#     print(filepath)
#     if os.path.exists(filepath):
#         print("{} is downloading by {}.....".format(fileSrc, username))
#         try:
#             with open(filepath, "rb") as src:
#                 data = src.read(1024)
#                 while data:
#                     client_socket.sendall(data)
#                     if len(data) < 1024:
#                         break
#                     data = src.read(1024)
#             client_socket.send("Download file sucess".encode("utf-8"))
#         except OSError as err:
#             print("Error opening file:", err)
#     else:
#         print("Source file does not exist.")
def handleDownload(client_socket, username, fileSrc, ftp):
    filename = os.path.basename(fileSrc)  # Extract only the filename
    print(f"{filename} is being downloaded by {username}...")

    try:
        def send_data(data):
            client_socket.sendall(data)
        ftp.retrbinary(f"RETR {filename}", send_data)
        client_socket.send("Download file success".encode("utf-8"))
        print("Download completed successfully.")
    except ftplib.error_perm as err:
        print("FTP error:", err)
        client_socket.send("Download failed: file not found or permission error.".encode("utf-8"))
    except Exception as err:
        # Handle general errors
        print("Error downloading file:", err)
        client_socket.send("Download failed.".encode("utf-8"))


def handleClient(client_socket, client_address):
    try:
        with ftplib.FTP("127.0.0.1") as ftp:
            username, password = handleLogin(client_socket)
            ftp.login(username, password)
            ftp.set_pasv(True)
            print(ftp.getwelcome())
            client_socket.send(ftp.getwelcome().encode("utf-8"))
            while True:
                data = client_socket.recv(1024)
                command = data.decode("utf-8")
                print("Message from client:", command)
                if command == 'exit':
                    # client_socket.send("exit".encode("utf-8"))
                    break
                elif command.startswith("upload "):
                    filedir = command.split()[1]
                    handleUpload(client_socket, filedir, username,ftp)
                elif command.startswith("download "):
                    fileSrc = command.split()[1]
                    handleDownload(client_socket, username, fileSrc)
                else:
                    client_socket.send("Command not found".encode("utf-8"))
    except client_socket.error as err:
        print("Error: ", err)
    finally:
        client_socket.close();


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    print("Server is listening port {}".format(port))
    try:
        while True:
            client_socket, client_address = s.accept()
            # handleClient(client_socket, client_address)
            thread = threading.Thread(target=handleClient, args=[client_socket, client_address], daemon=True)
            thread.start()
    except socket.error as err:
        print("Error: ", err)
    finally:
        s.close()
