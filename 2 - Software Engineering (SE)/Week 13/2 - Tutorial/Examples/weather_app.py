import requests

API_KEY = "API key from openweather"

MENU = """Weather4U
Please select an option below:
1. Current Weather
2. Weather History

0. Quit"""

def get_locations(location):
    payload = {
    'q' : location,
    'limit':5,
    'appid':API_KEY
    }
    response = requests.get("http://api.openweathermap.org/geo/1.0/direct", params=payload)
    return response.json()


def display_locations(locations):
    for i, location in enumerate(locations, 1):
        print(f"{i} - {location['name']}, {location['country']}")


def get_current_weather(lat, lon):
    payload = {
        'lat':lat,
        'lon':lon,
        'units':'metric',
        'appid':API_KEY,
    }
    response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=payload)
    return response.json()


def draw_line(symbol="-", length=80, prnt=False):
    line = (symbol * length)
    if prnt:
        print(line)
    return line + '\n'


def display_weather_data(data):
    overview = draw_line()
    overview += f"Weather Report: {data['name']} - {data['sys']['country']}"
    overview += draw_line()
    overview += f"{data['weather'][0]['description'].title()}\n"
    overview += f"Current Temp: {data['main']['temp']}\u00b0C\n"
    overview += f"Feels Like: {data['main']['feels_like']}\u00b0C\n"
    overview += f"Min Temp: {data['main']['temp_min']}\u00b0C\n"
    overview += f"Max Temp: {data['main']['temp_max']}\u00b0C\n"
    overview += draw_line()
    print(overview)


while True:
    user_option = input(MENU)
    if user_option == "1":
        location = input("Please enter a location: ")
        locations = get_locations(location)
        print("Please select a location below: ")
        display_locations(locations)
        index = int(input(": "))-1
        chosen_location = locations[index]
        current_weather = get_current_weather(chosen_location["lat"],
                                              chosen_location['lon'])
        display_weather_data(current_weather)
        input("Press enter to continue..")
    elif user_option == "0":
        break
