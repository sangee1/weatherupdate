from cgitb import text
import imp
import tkinter
import requests
import time
from win10toast import ToastNotifier
from bs4 import BeautifulSoup


def getWeather():
    city = "chennai"
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + \
        city + "&appid=cc28c69dcbf51d6b69ba3563c296bb2b"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    temp_min = int(json_data['main']['temp_min'] - 273.15)
    temp_max = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind_speed = json_data['wind']['speed']
    sunrise = time.strftime(
        "%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(
        json_data['sys']['sunset'] - 21600))
    #final_info = condition + '\n' + str(temp) + "°C"
    final_data = "Condition: " + condition + '\n' + "Temperature:" + str(temp) + "°C" + "\n" + "Max Temp:" + \
        str(temp_max) + "\n" + "Min Temp:" + \
        str(temp_min) + "\n" + "Pressure:" + str(pressure) + "\n" + \
        "Humidity:" + str(humidity) + "\n" + "Wind speed:" + str(wind_speed) + \
        "\n" + "Sunrise:" + str(sunrise) + "\n" + "Sun set:" + str(sunset)
    return final_data


n = ToastNotifier()
n._show_toast(title="Weather Update", icon_path=None,
              msg=getWeather(), duration=10)
