from geopy.geocoders import Nominatim
# initiate nominatim
# geolocator = Nominatim(user_agent="aaa515")
geolocator = Nominatim(user_agent="xxxxx@qq.com")  # 使用邮箱即可
# search for location
location = geolocator.geocode("长春市")
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)


