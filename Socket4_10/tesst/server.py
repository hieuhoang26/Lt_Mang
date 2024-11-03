from datetime import datetime
import socket
import os
import threading
import time

USER_DB = "D:\\LtMang\\testFile\\pass.txt"
FILE_DIR = "D:\\LtMang\\testFile\\data"
LOG = "D:\\LtMang\\testFile\\log.txt"
FILE_OWNER = "D:\\LtMang\\testFile\\file_ownership.txt"
host = "127.0.0.1"
port = 9096


# auth
def authenticate(username, password):
    try:
        with open(USER_DB, "r") as f:
            for line in f:
                user, pwd = line.strip().split(":")
                if user == username and pwd == password:
                    return True
    except FileNotFoundError:
        pass
    return False


def handleLogin(client_socket):
    authen = False
    while not authen:
        print("Connect Client: ", client_address)
        client_socket.send("Enter username:".encode("utf-8"))
        username = client_socket.recv(1024).decode("utf-8").strip()
        client_socket.send("Enter password:".encode("utf-8"))
        password = client_socket.recv(1024).decode("utf-8").strip()
        if authenticate(username, password):
            client_socket.send("200".encode("utf-8"))
            print("Login by {}".format(username))
            authen = True
            return username
        else:
            client_socket.send("401".encode("utf-8"))

def handleUpload(client_socket,filedir,username):
    if os.path.exists(filedir):
        filename = os.path.basename(filedir)
        filesize = os.path.getsize(filedir)
        print("{} is uploading.....".format(filename))
        filepath = os.path.join(FILE_DIR, f"{filename}")
        # filepath = os.path.join(FILE_DIR,filename)
        try:
            with open(f"{filepath}", "wb") as target:
                data = client_socket.recv(1024)
                while data:
                    target.write(data)
                    if len(data) < 1024:
                        break
                    data = client_socket.recv(1024)
            client_socket.send("File public/private? (y/n)".encode("utf-8"))
            response = client_socket.recv(1024).decode("utf-8").strip().lower()
            is_public = response == "y"
            set_owner(username, filename, is_public)
            log("upload",filename,username)
            client_socket.send("Upload file sucess".encode("utf-8"))
            print("Upload file sucesss")
        except OSError as err:
            print("Error opening file:", err)
    else:
        print("Source file does not exist.")

def handleDownload(client_socket,username,fileSrc):
    filepath = os.path.join(FILE_DIR,fileSrc)
    filename = os.path.basename(fileSrc)
    file_owner, access = get_owner(filename)
    print(file_owner,access)
    if os.path.exists(filepath) and (file_owner == username or access == "public"):
        print("{} is downloading by {}.....".format(fileSrc,username))
        try:
            with open(filepath, "rb") as src:
                client_socket.send("200".encode("utf-8"))
                data = src.read(1024)
                while data:
                    client_socket.sendall(data)
                    if len(data) < 1024:
                        break
                    data = src.read(1024)
            log("download", filename, username)
            client_socket.send("Download file sucess".encode("utf-8"))
            print("Download file sucesss")
        except OSError as err:
            print("Error opening file:", err)
    else:
        client_socket.send("403".encode("utf-8"))
        print("Permission denied to download this file.")
        # print("Source file does not exist.")


def log(action, filename, client_address):
    with open(LOG, "a") as log:
        log.write(f"{datetime.now()} - {client_address} - {action} - {filename}\n")
def read_log(keyword):
    results = ""
    with open(LOG, "r") as log_file:
        for line in log_file:
            if keyword in line:
                results += line
    return results if results else "No matching log entries found.\n"
def set_owner(username, filename, is_public=False):
    with open(FILE_OWNER, "a") as f:
        f.write(f"{username}:{filename}:{'public' if is_public else 'private'}\n")

def get_owner(filename):
    with open(FILE_OWNER, "r") as f:
        for line in f:
            user, file, access = line.strip().split(":")
            if file == filename:
                return user, access
    return None, None

def handleClient(client_socket, client_address):
    try:
        username = handleLogin(client_socket)
        while True:
            data = client_socket.recv(1024)
            command = data.decode("utf-8")
            print("Message from client:", command)
            if command == 'exit':
                # client_socket.send("exit".encode("utf-8"))
                break
            elif command.startswith("ls") or command.startswith("ls "):
                items = os.listdir(FILE_DIR)
                files_list = ""
                for item in items:
                    if os.path.isdir(os.path.join(FILE_DIR, item)):
                        files_list += f"*{item}\n"
                    else:
                        files_list += f"-{item}\n"
                client_socket.send(files_list.encode("utf-8"))
            elif command.startswith("log "):
                keyword = command.split()[1]
                rs = read_log(keyword)
                client_socket.send(rs.encode("utf-8"))
            elif command.startswith("upload "):
                filedir = command.split()[1]
                handleUpload(client_socket, filedir, username)
            elif command.startswith("download "):
                fileSrc = command.split()[1]
                handleDownload(client_socket,username,fileSrc)
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