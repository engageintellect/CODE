import pyowm
import subprocess
import colorama
from colorama import Fore

colorama.init()
subprocess.call('clear', shell=True)


owm = pyowm.OWM('e976803d50a2aeec31e749c537477b34')
mgr = owm.weather_manager()


location = 'Irvine, US'
subprocess.call('clear', shell=True)


sky_status = mgr.weather_at_place(location)
sky = sky_status.weather


def getWeather():
    weather = mgr.weather_at_place(location).weather
    temp_dict_fahrenheit = weather.temperature('fahrenheit')
    temp_now = temp_dict_fahrenheit['temp']
    temp_max = temp_dict_fahrenheit['temp_max']
    temp_min = temp_dict_fahrenheit['temp_min']
    feels_like = temp_dict_fahrenheit['feels_like']



    print(location.upper(), "", "\n")
    if sky.status == 'Clear':
        print("Current Conditions:  ", sky.status, " ")
    elif sky.status == 'Clouds':
        print("Current Conditions:  ", sky.status, " ")
    elif sky.status == 'Haze':
        print("Current Conditions:  ", sky.status, " ")
    print("Condition Details:   ", sky.detailed_status)
    print('\n')
    print("Current Temp:    ", temp_now, "F")
    print(Fore.RED + "High:            ", temp_max,"F")
    print(Fore.BLUE + "Low:             ", temp_min,"F")
    print(Fore.RESET + "Feels Like:      ", feels_like,"F")
    print('\n')



getWeather()

