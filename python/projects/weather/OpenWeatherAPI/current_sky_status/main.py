import pyowm

owm = pyowm.OWM('e976803d50a2aeec31e749c537477b34')
mgr = owm.weather_manager()

observation = mgr.weather_at_place('London,GB')  # the observation object is a box containing a weather object
weather = observation.weather

print(weather.status)           # short version of status (eg. 'Rain')
print(weather.detailed_status)  # detailed version of status (eg. 'light rain')
