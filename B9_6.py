# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 07:23:35 2024

@author: Acer
"""
import requests
import re

def extract_email(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.text # lay ve dang text
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9].[a-zA-Z]{2,}'
        emails = re.findall(email_pattern,data)
        # loc trung nhau
        # set_emails = set(emails)
        return emails
    except requests.RequestException as e:
        print(f"Error: {e}")
if __name__ =='_main_':
    url = 'https://en.wikipedia.org/wiki/Python'
    emails = extract_email(url)
    for i in emails:
        print(i)

