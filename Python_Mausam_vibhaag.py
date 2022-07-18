#python mausaam vibhaag

import datetime as dt
import requests

f=open("API.txt",'r')


def  wheather(dict):
    mosaum=dict['weather'][0]['description']
    temprature=dict['main']['temp']
    temprature-=273.15
    feels_like=dict['main']['feels_like']
    feels_like-=273.15
    min_temp=dict['main']['temp_min']
    min_temp-=273.15
    
    max_temp=dict['main']['temp_max']
    max_temp-=273.15
    humidity=dict['main']['humidity']
    visibility=dict['visibility']
    temprature =str(round(temprature,2))
    feels_like=str(round(feels_like,2))
    min_temp = str(round(min_temp, 2))
    max_temp = str(round(max_temp, 2))
    print("Today it is ",mosaum)
    print("Temprature ",temprature,"c")
    print("Feels Like ",feels_like,"c")
    print("Minimum Temprature ",min_temp)
    print("Maximum Temprature ",max_temp)
    print("Humidity ",humidity ,"%")
    print("Visibility ",visibility )
BASE_URL="http://api.openweathermap.org/data/2.5/weather?"
API_KEY=f.read()
CITY="New Delhi"
url=BASE_URL+"appid="+API_KEY+"&q="+CITY
response=requests.get(url).json()


a=wheather(response)
