# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 07:37:06 2024

@author: Acer
"""

import ftplib
def list_direc(ftp):
    print("_____List Direc_____")
    try:
        files = []
        ftp.dir(files.append)
        return files
        
    except ftplib.all_errors as e:
        print(f"Error listing direc: {e}" )
        return []

def change_directory(ftp, direc):
    print("_____Change Direc_____")
    try:
        ftp.cwd(direc)
        print(f"Changed to {direc}")
        
    except ftplib.all_errors as e:
        print(f"Error Change direc: {e}" )
        return []
def create_direc (ftp, direc):
    print("_____Create Direc_____")
    try:
        ftp.mkd(direc)
        print(f"Created to {direc}")
    except ftplib.all_errors as e:
        print(f"Error Create direc: {e}" )
        return []
def delete_file (ftp, direc):
    print("_____Delete Direc_____")
    try:
        ftp.delete(direc)
        print(f"Created to {direc}")
    except ftplib.all_errors as e:
        print(f"Error Delete direc: {e}" )
        return []
def delete_direc (ftp, direc):
    print("_____Delete Direc_____")
    try:
        ftp.rmd(direc)
        print(f"Created to {direc}")
    except ftplib.all_errors as e:
        print(f"Error Delete direc: {e}" )
        return []
def rename (ftp,name1, name2):
    print("_____Rename Direc_____")
    try:
        ftp.rename(name1,name2)
        print(f"Created to {name2}")
    except ftplib.all_errors as e:
        print(f"Error Rename direc: {e}" )
        
def size (ftp,name):
    print("_____Size Direc_____")
    try:
        size = ftp.size(name)
        print(f"Size {name} : {size}")
    except ftplib.all_errors as e:
        print(f"Error Size direc: {e}" )
        return None
def download (ftp,file,file_copoy):
    print("_____Down Direc_____")
    try:
       with open(file_copy, "rb") as fp:
           ftp.retrbinary("RETR" + file,fp.write)
    
    except ftplib.all_errors as e:
        print(f"Error Downloading direc: {e}" )
        if os.path.isFile(file_copy):
            os.remove(file_copoy)
        return None
def upload (ftp,file):
    print("_____Upload Direc_____")
    try:
       with open(file, "rb") as fp:
           res = ftp.strobinary("STOR" + file,fp)
           print(f" Response: {res}")
    except ftplib.all_errors as e:
        print(f"Error Downloading direc: {e}" )
        return None
    
def print_menu():
    print("\menu")
    print("1. List direc")
    print("2. Change direc")
    print("3. Create direc")
    print("4. Del file")
    print("5. Del direc")
    print("6. Rename file or direc")
    print("7. Get file size")
    print("8. Download file")
    print("9. Upload file")
    print("10. Send custom command")
    print("11. Exit")
