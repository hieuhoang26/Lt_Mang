import urllib.request
print('starting download')
url = 'https://www.python.org/static/img/python-logo@2x.png'
urllib.request.urlretrieve(url,'python.png')
with urllib.request.urlopen(url) as r:
    print('status:', r.status)
    print('downloading')
    with open('python.png', 'wb') as image:
        image.write(r.read())
