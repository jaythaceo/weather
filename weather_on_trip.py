from geopy.geocoders import Nominatim
from datetime import datetime, timedelta
import sys, requests

#Dark_Sky_API_KEY = ""
option_list = "exclude=currently, minutely,hourly,alerts&units=si"

if (len(sys.argv) < 4):
	print("Usage: python weather_on_trip.py <address> <Start Date in YYYY-MM-DD <End Date in YYYY-MM-DD>")
	sys.exit()

location = Nominatim().geocode(sys.argv[1], language='en_US')


