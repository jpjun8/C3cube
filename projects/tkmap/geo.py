from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent = 'gmap')
loc = geolocator.geocode("경주")
print(loc.address)