import pyowm

owm = pyowm.OWM('e976803d50a2aeec31e749c537477b34')
mgr = owm.weather_manager()

location = input("Please enter a location: ")
weather = mgr.weather_at_place(location).weather


temp_dict_fahrenheit = weather.temperature('fahrenheit')

# temp_now = temp_dict_fahrenheit['temp']
# temp_min = temp_dict_fahrenheit['temp_min']
# temp_max = temp_dict_fahrenheit['temp_max']
# feels_like = temp_dict_fahrenheit['feels_like']


for key in temp_dict_fahrenheit:
    print(key, temp_dict_fahrenheit[key])


