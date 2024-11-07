import urllib.request
import urllib.parse
import gzip
import webbrowser


# Retrieve the HTML page's code from a URL
def fetch_webpage(url):
    try:
        with urllib.request.urlopen(url) as response:
            print(response.status)
            # html = response.read() #the response is a sequence of bytes
            html = response.read().decode('utf-8')  # convert sequence of bytes to string
            print(html)

    except urllib.error.URLError as e:
        print(f"Error fetching webpage: {e}")
        return None


# Example 1.1: Simple GET request
def simple_get_request():
    url = "https://www.example.com"
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    print(data)


# Example 1.2: POST request with parameters (Error)
def post_request_with_parameters():
    url = "https://www.example.com/submit_data"
    params = {
        "name": "John Doe",
        "email": "john@example.com"
    }
    data = urllib.parse.urlencode(params).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    print(result)


# Example 2.1: Basic usage of add_header
def basic_add_header():
    req = urllib.request.Request('http://google.com')

    # req.add_header("Accept-Language", "en")
    # response = urllib.request.urlopen(req)
    # print(*response)

    req.add_header("Accept-Encoding", "gzip")
    response = urllib.request.urlopen(req)
    data = gzip.decompress(response.read())

    print(data)
    # print(response.getheaders())


if __name__ == "__main__":
    post_request_with_parameters()