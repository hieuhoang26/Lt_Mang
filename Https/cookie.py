# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 07:31:52 2024

@author: Acer
"""

from urllib.request import urlopen
from http.cookiejar import cookiejar
from urllib.request import build_opener,HTTPCookieProcessor
import datetime

if __name__=='__main__':
    r = request('')
    r1= urlopen(r)
    print(r1.url)
    print(r1.get_header('User-agent'))
    print(r.redirect_dict)
#cookie
if __name__=='__main__':
    cj = cookiejar()
    opener = build_opener(HTTPCookieProcessor())
    r= opener.open('')
    print(len(cj))
    cookies = list(cj)
    print(cookies)
    print(cookies[1].name)
    print(datetime.datetime.fromtimestamp(cookies[1].expires))