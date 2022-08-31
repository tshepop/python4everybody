import urllib.request
import urllib.parse
import urllib.error
from geopy.geocoders import Nominatim
import json

"""
I chose to use the Geopy library for geolocation, instead of the google maps API geocode.
Geopy is able to retrieve different services that provide APIs and implements accessing these
different services in a single package. OpenStreetMap is open source.
"""

geolocator = Nominatim(user_agent="my_locations")

address_inp = input("Enter address: ")
