# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 07:27:38 2024

@author: Dung Dang
"""

import ftplib
import os

def list_directory(ftp):
    print("_____Function List Directory_____")
    try:
        files = []
        ftp.dir(files.append())
        return files
        
    except ftplib.all_errors as e:
        print(f"Error listing directory: {e} ")
        return []

def change_directory(ftp, directory):
    print("_____Function Change Directory_____")
    try:
        ftp.cwd(directory)
        print(f"Change to directory: {directory} ")
        
    except ftplib.all_errors as e:
        print(f"Error changing directory: {e} ")

def create_directory(ftp,directory):
    print("_____Function Create Directory_____")
    try:
        ftp.mkd(directory)
        print(f"Create directory : {directory}")
        
    except ftplib.all_errors as e:
        print(f"Error creating directory: {e} ")

def delete_file(ftp, filename):
    print("_____Function Delete File_____")
    try:
        ftp.delete(filename)
        print(f"Deleted file: {filename}")
        
    except ftplib.all_errors as e:
        print(f"Error deleting file: {e} ")
        
def delete_directory(ftp, directoryname):
    print("_____Function Delete Directory_____")
    try:
        ftp.rmd(directoryname)
        print(f"Deleted directory: {directoryname}")
        
    except ftplib.all_errors as e:
        print(f"Error deleting directory: {e} ")

def rename_file_or_directory(ftp, fromname, toname):
    print("_____Function Rename File Or Directory_____")
    try:
        ftp.rename(fromname,toname)
        print(f"Renamed {fromname} to {toname}")
        
    except ftplib.all_errors as e:
        print(f"Error renaming file or directory: {e} ")

def get_file_size(ftp,filename):
    print("_____Function Get File Size_____")
    try:
        size = ftp.size(filename)
        print(f"Size of {filename}: {size} bytes")
        return size
        
    except ftplib.all_errors as e:
        print(f"Error getting file size: {e} ")
        return None
    
def download_file(ftp, file_origin, file_copy):
    print("_____Function Download File_____")
    try:
        with open(file_copy, "wb") as fp:
            ftp.retrbinary("RETR " + file_origin, fp.write())
        print(f"Download of {file_origin} to {file_copy} completed successfull")
        
    except ftplib.all_errors as e:
        print(f"Error downloading file: {e} ")
        if os.path.isfile(file_copy):
            os.remove(file_copy)

def upload_file(ftp, file_name):
    print("_____Function Upload File_____")
    try:
        with open(file_name, "rb") as fp:
            response = ftp.storbinary("STOR " + filename, fp)
        print(f"Server response: {response}")
        
        if not response.startwith("226"):
            print("Upload failed !")
        else:
            print(f"Upload file {file_name} completed successfully")
        
    except ftplib.all_errors as e:
        print(f"Error uploading file: {e} ")
        
def send_custom_command(ftp, command):
    print("_____Function Send Custom Command_____")
    try:
        response = ftp.sendcmd(command)
        return response
        
    except ftplib.all_errors as e:
        print(f"Error sending command: {e} ")
        
def print_menu():
    print("\nMenu:")
    print("1. List directory")
    print("2. Change directory")
    print("3. Create directory")
    print("4. Delete file")
    print("5. Delete directory")
    print("6. Rename file or directory")
    print("7. Get file size")
    print("8. Download file")
    print("9. Upload file")
    print("10. Send custom command")
    print("11. Exit")

if __name__ == "__main__":
    with ftplib.FTP("127.0.0.1") as ftp:
        try:
            ftp.login("User01","123")
            ftp.set_pasv(True)
            
            print(ftp.getwelcome())
            
            while True:
                print_menu()
                choice = input("Enter your choice: ")
                
                if choice == "1":
                    entries = list_directory(ftp)
                    print(len(entries)," entries:")
                    for entry in entries:
                        print(entry)
                elif choice == "2":
                    directory = input("Enter directory name to change to: ")
                    change_directory(ftp, directory)
                elif choice == "3":
                    directory = input("Enter directory name to create: ")
                    create_directory(ftp, directory)
                elif choice == "4":
                    filename = input("Enter file name to delete: ")
                    delete_file(ftp, filename)
                elif choice == "5":
                    directoryname = input("Enter directory name to delete: ")
                    delete_directory(ftp, directoryname)
                elif choice == "6":
                    fromname = input("Enter current name file or directory want to change: ")
                    toname = input("Enter new name: ")
                    rename_file_or_directory(ftp, fromname, toname)
                elif choice == "7":
                    filename = input("Enter file name want to check: ")
                    get_file_size(ftp, filename)
                elif choice == "8":
                    file_origin = input("Enter file want to download: ")
                    file_copy = input("Enter local path and filename to save as: ")
                    download_file(ftp, file_origin, file_copy)
                elif choice == "9":
                    file_name = input("Enter file name want to upload: ")
                    upload_file(ftp, file_name)
                elif choice == "10":
                    command = input("Enter custom FTP command: ")
                    response = send_custom_command(ftp, command)
                elif choice == "11":
                    print("Exit....")
                    break
                else :
                    print("Invalid choice. Please try again")
            
        except ftplib.all_errors as e:
            print(f"FTP error: {e}")
            