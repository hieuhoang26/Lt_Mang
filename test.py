import requests

# url = 'http://api.github.com'
# r = requests.get(url)
# print(r.json())

url = 'https://pixabay.com/en/photos/search/'
prams = {
    'q': 'tiger',
    'order': 'popular',
    'min_width': '800',
    'min_height': '600',
}
r = requests.get(url, params=prams)
print(r.url)
