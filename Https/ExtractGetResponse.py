
# Https Get

import requests
def get_geo_info(url):
    try:
        # Send a GET request to the URL
        r = requests.get(url)

        # Print the HTTP status code
        print("HTTP code:", r.status_code)

        # Print response headers
        print("Response Headers:")
        for header, val in r.headers.items():
            print(f"{header}: {val}")

        # If the status code is 200, process the JSON data
        if r.status_code == 200:
            data = r.json()

            # Print JSON data
            print("JSON Response Data:")
            for key, value in data.items():
                print(f"{key}: {value}")

            # Print request headers
            print("Request Headers:")
            for header, val in r.request.headers.items():
                print(f"{header}: {val}")

            # Print server info from response headers
            if 'server' in r.headers:
                print("Server:", r.headers['server'])
        else:
            # Print error if the status code is not 200
            print("Error: HTTP status code", r.status_code)

    except requests.RequestException as e:
        # Handle any request-related errors
        print(f"Error: {e}")


if __name__ == '__main__':
    # Define the URL and call the function
    url = 'https://httpbin.org/get'
    get_geo_info(url)
