from geopy.geocoders import Nominatim
from datetime import datetime, timedelta
import sys, requests

#Dark_Sky_API_KEY = ""
option_list = "exclude=currently, minutely,hourly,alerts&units=si"

if (len(sys.argv) < 4):
	print("Usage: python weather_on_trip.py <address> <Start Date in YYYY-MM-DD <End Date in YYYY-MM-DD>")
	sys.exit()

location = Nominatim().geocode(sys.argv[1], language='en_US')

if location == None:
	print("location not found")
	sys.exit()

d_from_date = datetime.strptime(sys.argv[2], '%Y-%m-%d')
d_to_date = datetime.strptime(sys.argv[3], '%Y-%m-%d')
delta = d_to_date - d_from_date

latitude = str(location.latitude)
longitude = str(location.longitude)

print("\nLocation: "+ location.address)
