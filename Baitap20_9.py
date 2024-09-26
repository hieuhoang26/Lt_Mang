"""
Created on Sun Sep 22 01:12:38 2024

@author: Martin Valentine
"""

""" 
1. Dùng thư viện googlemap tính khoảng cách từ 2 địa điểm cho trước. 
Hiện tại Google Maps ko hỗ trợ API ở VNam (đang bị giới hạn) nên sẽ sử dụng openrouteservice.

2. Check nước, timezone từ ip cho trước.

3. Check ip từ website cho trước.
"""

"""
********** Requirements **********

pip install openrouteservice
pip install geoip2
pip install dnspython
"""

import openrouteservice
import geoip2.database
import dns.resolver

def get_route():
    """Fetches route information between two addresses."""
    # Set up API key
    ors_api_key = input("Enter your OpenRouteService API key: ")
    client = openrouteservice.Client(key=ors_api_key)
    
    # Get start and destination
    start = input("Enter your start address: ")
    destination = input("Enter your destination address: ")
    
    # Geocode start location
    start_coords = client.pelias_search(start)['features'][0]['geometry']['coordinates']
    # Geocode destination location
    destination_coords = client.pelias_search(destination)['features'][0]['geometry']['coordinates']
    
    # Get route
    route = client.directions(
        coordinates=[start_coords, destination_coords],
        profile='driving-car',
        format='geojson'
    )

    # Extract distance and duration
    distance = route['features'][0]['properties']['segments'][0]['distance'] / 1000  # meters to kilometers
    duration = route['features'][0]['properties']['segments'][0]['duration'] / 60  # seconds to minutes
    
    # Print route information
    print(f"Start: {start}")
    print(f"Destination: {destination}")
    print(f"Distance: {distance} Km")
    print(f"Estimated Duration: {duration} mins")

    return

def get_ip_info(ipaddr):
    """Fetches country, continent, and timezone information for a given IP address."""
    # download database in this https://g...content-available-to-author-only...b.com/P3TERX/GeoLite.mmdb
    
    # Lookup IP address
    reader = geoip2.database.Reader('F:/UTC/SEMESTER 7/Network Programming/Code/GeoLite2-City.mmdb')  # Path to Database 
    response = reader.city(ipaddr)

    if response is not None:
        print("Country: ", response.country.name)
        print("Continent: ", response.continent.name) 
        print("Timezone: ", response.location.time_zone)  # https://m...content-available-to-author-only...b.io/GeoIP2-php/doc/v2.8.0/class-GeoIp2.Record.Location.html
    else:
        print("No information found for this IP address.")
    
    # Close the reader
    reader.close()

def get_domain_info(target_domain):  # https://m...content-available-to-author-only...m.com/@jsquared7/dns-enumeration-using-python-772bbeea7b0e
    """Fetches DNS records for a given domain."""
    # Set the record type
    record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]
    
    # Create a DNS resolver
    resolver = dns.resolver.Resolver()
    
    for record_type in record_types:
        # Performs DNS lookup for the defined domain and record type
        try:
            answers = resolver.resolve(target_domain, record_type)
        except dns.resolver.NoAnswer:
            continue
        
        # Prints the results
        print(f"{record_type} records for {target_domain}:")
        for rdata in answers:
            print(f" {rdata}")
        
    return

if __name__ == "__main__":
    
    """
    Test data:
        Route:
            {API Key cua ban}  Truy cap https://o...content-available-to-author-only...e.org/
            Ha Noi
            Noi Bai International Airport, Phú Minh, Sóc Sơn, Hà Nội, Vietnam
            
        IP: 104.244.42.129
        
        Domain: facebook.com
            
    """
    
    # Get route
    route_info = get_route()
    print("\n ************** end function **************\n")
    
    # Get IP address information
    ip = input("Enter IP address: ")
    get_ip_info(ip)
    print("\n ************** end function **************\n")
    
    # Get domain
    domain = input("Enter domain: ")
    get_domain_info(domain)
    print("\n ************** end function **************\n")

    