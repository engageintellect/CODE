import pyowm

owm = pyowm.OWM('e976803d50a2aeec31e749c537477b34')
mgr = owm.weather_manager()

location = "los angeles, us"

weather =  mgr.weather_at_zip_code('92620', 'us').weather

temp_dict = weather.temperature(unit='fahrenheit')



mylist = [
    temp_dict['temp'],
    temp_dict['feels_like'],
    temp_dict['temp_max'],
    temp_dict['temp_min'],
]



sunrise = weather.sunrise_time(timeformat='iso')
sunset = weather.sunset_time(timeformat='iso')
wind = weather.wind(unit='miles_hour')
icon = weather.weather_icon_url(size=" ")


print(weather)
print(sunrise)
print(sunset)
print(wind)
print(icon)


print(mylist)






