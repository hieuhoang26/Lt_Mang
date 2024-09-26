# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 07:43:29 2024

@author: Acer
"""

import requests

def get_geo_info(url):
    try:
        r = requests.get(url)
        r.raise_for_status()   
        geo_info = r.json()
        print('Ip address:', geo_info.get('ip'))
        print('Country: ', geo_info.get('country'))
        print('Region: ', geo_info.get('region'))
        print('City: ', geo_info.get('city'))
        # print('Zip Code: ', geo_info.get('zipcode'))
        # print('Latitude: ', geo_info.get('latitude'))
        # print('Longtitude: ', geo_info.get('Longtitude'))
    except requests.RequestException as e:
        print(f"Error: {e}")
        
        
        
if __name__ =='_main_':
    url = 'https://ipinfo.io/111.65.249.59/json'
    get_geo_info(url)
   