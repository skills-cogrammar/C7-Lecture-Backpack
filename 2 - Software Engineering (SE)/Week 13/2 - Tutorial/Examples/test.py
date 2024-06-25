import requests

API_KEY = "API key from OpenWeather"

payload = {
    'q' : "London",
    'limit':5,
    'appid':API_KEY
}
response = requests.get("http://api.openweathermap.org/geo/1.0/direct", params=payload)

location = response.json()[0]

print(location['name'])
print(location['lat'])
print(location['lon'])

lat = location['lat']
lon = location['lon']

payload = {
    'lat':lat,
    'lon':lon,
    'appid':API_KEY,
}
response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=payload)

print(response.text)