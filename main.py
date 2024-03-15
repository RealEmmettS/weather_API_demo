import requests
import re
import json
import geopy
from geopy.geocoders import Nominatim

import os

lat = None
lon = None
parameters = None

usrLoc = input("Enter location to check: ")


geolocator = Nominatim(user_agent="iCode_Weather_Machine")
try:
	location = geolocator.geocode(usrLoc)
	lat = location.latitude
	lon = location.longitude
	parameters = {
		"lat": lat,
		"lon": lon
	}
except:
	print("\nThat's not a valid location. Please enter a place name or an address.")


print("Repairing lat and lon values...")
for x in range(1, 1000):
	if lat<-90:
		lat+=2
	if lat>90:
		lat-=2
	if lon<-180:
		lon+=2
	if lon>180:
		lon-=2
else:
	print("Done repairing.\n")




appid = os.getenv('APP_ID')

weather_api_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={appid}"

response = requests.get(weather_api_url)
json = response.json()


main = json['main']
current_temp = main['temp']
print("\n\nThe current temperature is: "+str(current_temp))


# REMEMBER !!!
# When running the program, enter the location as "CITY, ST" every time. 
#	For example:
#		- Frisco, TX
#		- Dallas TX