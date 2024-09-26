# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 08:05:00 2024

@author: Acer
"""

import requests

def get_geo_info(url):
    try:
        r = requests.get(url)
        print("Http code" + str(r.status_code))
        
        print(r.headers)
        if r.status_code == 200:
            data = r.json()
            for d in data.items():
                print(d)
            print("Header response")
            for header, val in r.headers.items():
                print(header,"--",val)
            print("Header requests")
            
            for header, val in r.request.headers.items():
                print(header,"--",val)
            print("server"+ r.headers['server'])
        else:
            print("err: %s" %r.status_code)
       
    except requests.RequestException as e:
        print(f"Error: {e}")
        
        
        
if __name__ =='_main_':
    url = 'https://httpbin.org/get'
    get_geo_info(url)
   