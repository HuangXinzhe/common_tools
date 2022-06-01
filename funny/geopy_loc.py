from geopy.geocoders import Nominatim
# initiate nominatim
geolocator = Nominatim(user_agent="aaa515")
# search for location
location = geolocator.geocode("合肥")
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)