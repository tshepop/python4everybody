from distutils.log import info
import urllib.request
import urllib.parse
import urllib.error
from geopy.geocoders import Nominatim
import json

"""
I chose to use the Geopy library for geolocation, instead of the google maps API geocode.
Geopy is able to retrieve different services that provide APIs and implements accessing these
different services in a single package. OpenStreetMap is open source.

install geopy on Ubuntu
sudo apt-get install geopy

"""

geolocator = Nominatim(user_agent="my_locations")

address_inp = input("Enter latitude and longitude: ")

location = geolocator.reverse(address_inp)
loc_dict = location.raw
print(type(loc_dict))

# convert python obj into json string
info = json.dumps(loc_dict, indent=4)
print(info)
