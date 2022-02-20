#This is a python code to locate anyone's address using IP Address
import urllib.request
import os
import json
import geopy.geocoders


ip = input('Enter The IP Adress: ')
url = "http://ip-api.com/json/"
with urllib.request.urlopen(url + ip) as response:
    data = response.read()
values = json.loads(data)

print(values)
lat = values['lat']
lon = values['lon']
geolocator = geopy.Nominatim(user_agent="reverse_locator")
address = geolocator.reverse(f'{lat},{lon}')
print(address)
