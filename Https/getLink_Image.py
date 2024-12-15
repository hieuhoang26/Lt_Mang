import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
# url = urlopen('https://en.wikipedia.org/wiki/Python')
# bs = BeautifulSoup(url)
# get all link
# for link in bs.find_all("a"):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

# get all image
# for img in bs.find_all("img"):
#     if 'src' in img.attrs:
#         print(img.attrs['src'])

# get link all image
url = 'https://en.wikipedia.org/wiki/Python'
header = requests.utils.default_headers()
r = requests.get(url,headers=header)
bs = BeautifulSoup(r.content,'html.parser')
images = bs.find_all('img')
print('total', len(images))
for i in images:
    print(i['src'])

# from urllib.request import urlopen,Request
# r=Request('https://vnexpress.net/')
# r1=urlopen(r)
# string = str(r1.read())
# count = string.count('.jpg')   //png
# print(count)
