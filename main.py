# Upload on github: https://github.com/psycholsc/WeatherForecast
# I'm still updating it!
# Format autopep8
import re
import os
import socket
import time
import json
import requests
from Alert import Alert as Alt
import Alert
AlertObj = Alt()
t0 = time.time()


def shutdown():
    '''shut down'''
    AlertObj.Info(
        "Finish all in {} s".format(time.time() - t0),
        color=Alert.FOREGROUND_WHITE)
    os.system('pause')
    exit()


# ================================================================
'''
Weather Infomation Analysis
Updated after new HeWeather API released. 
'''


class WeatherInfo(object):
    def __init__(self, weather_dict):
        if weather_dict['HeWeather6'][0]['status'] == 'ok':
            AlertObj.Info('Status OK.')
        else:
            AlertObj.Warn("Unable to get Weather Data!")
            shutdown()
        WeatherData = weather_dict['HeWeather6']
        WeatherData = WeatherData[0]
        # print(WeatherData)
        # daily_forecast
        self.daily = WeatherData['daily_forecast']
        # today
        self.today_cond_day = self.daily[0]['cond_txt_d']
        self.today_cond_night = self.daily[0]['cond_txt_n']
        self.today_date = self.daily[0]['date']
        self.today_humidity = self.daily[0]['hum']  # percentage
        self.today_moonrise = self.daily[0]['mr']
        self.today_moonset = self.daily[0]['ms']
        self.today_sunrise = self.daily[0]['sr']
        self.today_sunset = self.daily[0]['ss']
        self.today_precipitation = self.daily[0]['pcpn']  # millimeter
        self.today_rainy_percentage = self.daily[0]['pop']  # percentage
        self.today_presure = float(self.daily[0]['pres']) / 10  # kPa

        self.today_temperature_min = self.daily[0]['tmp_min']  # Degree Celsius
        self.today_temperature_max = self.daily[0]['tmp_max']  # Degree Celsius
        self.today_uv = self.daily[0]['uv_index']
        self.today_visibility = self.daily[0]['vis']  # visualability km
        self.today_wind_deg = self.daily[0]['wind_deg']
        self.today_wind_dir = self.daily[0]['wind_dir']
        self.today_wind_power = self.daily[0]['wind_sc']
        self.today_wind_windspeed = self.daily[0]['wind_spd']  # kmph
        # tomorrow
        self.tomorrow_cond_day = self.daily[1]['cond_txt_d']
        self.tomorrow_cond_night = self.daily[1]['cond_txt_n']
        self.tomorrow_date = self.daily[1]['date']
        self.tomorrow_humidity = self.daily[1]['hum']  # percentage
        self.tomorrow_moonrise = self.daily[1]['mr']
        self.tomorrow_moonset = self.daily[1]['ms']
        self.tomorrow_sunrise = self.daily[1]['sr']
        self.tomorrow_sunset = self.daily[1]['ss']
        self.tomorrow_precipitation = self.daily[1]['pcpn']  # millimeter
        self.tomorrow_rainy_percentage = self.daily[1]['pop']  # percentage
        self.tomorrow_presure = float(self.daily[1]['pres']) / 10  # kPa
        # Degree Celsius
        self.tomorrow_temperature_min = self.daily[1]['tmp_min']
        # Degree Celsius
        self.tomorrow_temperature_max = self.daily[1]['tmp_max']
        self.tomorrow_uv = self.daily[1]['uv_index']
        self.tomorrow_visibility = self.daily[1]['vis']  # visualability km
        self.tomorrow_wind_deg = self.daily[1]['wind_deg']
        self.tomorrow_wind_dir = self.daily[1]['wind_dir']
        self.tomorrow_wind_power = self.daily[1]['wind_sc']
        self.tomorrow_wind_windspeed = self.daily[1]['wind_spd']  # kmph
        # The day after:
        self.tda_cond_day = self.daily[2]['cond_txt_d']
        self.tda_cond_night = self.daily[2]['cond_txt_n']
        self.tda_date = self.daily[2]['date']
        self.tda_humidity = self.daily[2]['hum']  # percentage
        self.tda_moonrise = self.daily[2]['mr']
        self.tda_moonset = self.daily[2]['ms']
        self.tda_sunrise = self.daily[2]['sr']
        self.tda_sunset = self.daily[2]['ss']
        self.tda_precipitation = self.daily[2]['pcpn']  # millimeter
        self.tda_rainy_percentage = self.daily[2]['pop']  # percentage
        self.tda_presure = float(self.daily[2]['pres']) / 10  # kPa
        self.tda_temperature_min = self.daily[2]['tmp_min']  # Degree Celsius
        self.tda_temperature_max = self.daily[2]['tmp_max']  # Degree Celsius
        self.tda_uv = self.daily[2]['uv_index']
        self.tda_visibility = self.daily[2]['vis']  # visualability km
        self.tda_wind_deg = self.daily[2]['wind_deg']
        self.tda_wind_dir = self.daily[2]['wind_dir']
        self.tda_wind_power = self.daily[2]['wind_sc']
        self.tda_wind_windspeed = self.daily[2]['wind_spd']  # kmph
        # aqi
        try:
            self._aqi = WeatherData['aqi']
            self.pm10 = self._aqi['city']['pm10']
            self.pm25 = self._aqi['city']['pm25']
            self.aqi = self._aqi['city']['aqi']
            self.co = self._aqi['city']['co']
            self.no2 = self._aqi['city']['no2']
            self.o3 = self._aqi['city']['o3']
            self.so2 = self._aqi['city']['so2']
            self.qlty = self._aqi['city']['qlty']
        except:
            AlertObj.Warn("Some Information not found in aqi section.")
        # basic information
        self.basic = WeatherData['basic']
        self.latitude = self.basic['lat']
        self.longitude = self.basic['lon']
        self.updatetime_loc = WeatherData['update']['loc']
        self.updatetime_utc = WeatherData['update']['utc']
        # now
        self.now = WeatherData['now']
        self.now_cond = self.now['cond_txt']
        self.now_feel = self.now['fl']  # sendible temperature
        self.now_temperature = self.now['tmp']
        self.now_humidity = self.now['hum']  # percentage
        self.now_precipitation = self.now['pcpn']  # millimeter
        self.now_presure = float(self.now['pres']) / 10  # kPa
        self.now_vis = self.now['vis']
        self.now_wind_deg = self.now['wind_deg']
        self.now_wind_dir = self.now['wind_dir']
        self.now_wind_power = self.now['wind_sc']
        self.now_wind_windspeed = self.now['wind_spd']
        AlertObj.Info(
            "Finish analyzing weather data", color=Alert.FOREGROUND_WHITE)


# ================================================================
# Get Your IP Addr.
s = requests.session()
# Solution I:
ip_url = "http://www.trackip.net/ip"
r = requests.get(ip_url)
if r.status_code == 200:
    ip = r.content.decode()
elif r.status_code == 403:
    r = eval(requests.get(
        'http://www.trackip.net/ip?json').content.decode())['IP']
else:
    # Solution II:
    ip_url = ["http://www.trackip.net/", 'http://www.ip.cn/']
    for i in range(len(ip_url)):
        urlstring = requests.get(ip_url[i]).content
        ip = re.findall(b'\d+\.\d+\.\d+\.\d+', urlstring)[0].decode()
        if ip == '' and i != len(ip_url) - 1:
            AlertObj.Warn("Fail to get your IP Address({} Try)".format(i + 1))
            continue
        elif ip == '' and i == len(ip_url) - 1:
            AlertObj.Warn(
                "Fail to get your IP Address at the moment.Please check your Network")
            os.system('pause')
            exit()
# Finish getting IP
hostname = socket.gethostname()
AlertObj.Info("Hello %s user." % hostname, color=Alert.FOREGROUND_WHITE)
AlertObj.Info("Your IPv4 Address:    {}".format(ip))
# Get Location
# Solution I
location_url = 'http://freeapi.ipip.net/'
r = requests.get(location_url + ip)
# print(r.content.decode())
location = eval(r.content.decode())[0:3]
# print(location)
city = eval(r.content.decode())[2]
ISP = eval(r.content.decode())[3]
if '' in location:
    AlertObj.Warn('No City Info of your IP.')
    exit()
AlertObj.Info(
    "============================================================",
    color=Alert.FOREGROUND_WHITE)
AlertObj.Info("According to your IP Addr, you are now in {} {} {}".format(
    location[0], location[1], location[2]))
# AlertObj.Info("Weather Forecast for {}".format(city))
'''
with open('tmp.json', 'r', encoding='utf-8') as f:
    weather_dict = json.loads(f.read())
    print(type(weather_dict))
    Wobj = WeatherInfo(weather_dict)
    exit()
'''
# Get Weather Infomation.
# API: https://free-api.heweather.com/s6/weather?parameters
key = ''
if key == '':
    print('please buy a key by yourself.')
    shutdown()
url = 'https://free-api.heweather.com/s6/weather'
parameters = {
    'location': city,
    'key': key,
}
s = requests.session()
r = requests.get(url, params=parameters)
weather_dict = json.loads(r.content.decode())
Wobj = WeatherInfo(weather_dict)
# Temperature
tempColor = Alert.FOREGROUND_WHITE
if float(Wobj.latitude) >= 0:
    lat = 'N'
else:
    lat = 'S'
if float(Wobj.longitude) >= 0:
    lon = 'E'
else:
    lon = 'W'
AlertObj.Info(
    "============================================================",
    color=Alert.FOREGROUND_WHITE)
AlertObj.Info("Weather Forecast for {}".format(city))
AlertObj.Info(
    "latitude:      {}°{}\n\t\t longitude:     {}°{}".format(
        Wobj.latitude, lat, Wobj.longitude, lon),
    color=Alert.FOREGROUND_WHITE)
AlertObj.Info(
    "============================================================",
    color=Alert.FOREGROUND_WHITE)

if int(Wobj.now_temperature) >= 33 or int(Wobj.now_feel) >= 33:
    tempColor = Alert.FOREGROUND_RED
elif 25 <= int(Wobj.now_temperature) < 33 and 25 <= int(Wobj.now_feel) < 33:
    tempColor = Alert.FOREGROUND_YELLOW
elif 16 < int(Wobj.now_temperature) < 25 and 16 < int(Wobj.now_feel) < 25:
    tempColor = Alert.FOREGROUND_GREEN
else:
    tempColor = Alert.FOREGROUND_BLUE
AlertObj.Info(
    "Real Time Weather: \n\t\t Condition: {}    Temperature: {}℃\n\t\t Sendible Temperature: {}℃ ".
    format(Wobj.now_cond, Wobj.now_temperature, Wobj.now_feel),
    color=tempColor)
AlertObj.Info(
    "Humidity: {}%  Precipitation :{}mm\n\t\t Pressure: {}kPa".format(
        Wobj.now_humidity, Wobj.now_precipitation, Wobj.now_presure))
AlertObj.Info(
    "============================================================",
    color=Alert.FOREGROUND_WHITE)
AlertObj.Info("Today: {}".format(Wobj.today_date))
AlertObj.Info("Condition in day:   {}\n\t\t Condition at night: {}".format(
    Wobj.today_cond_day, Wobj.today_cond_night))
if int(Wobj.today_temperature_min) >= 33:
    tempColor = Alert.FOREGROUND_RED
elif 25 <= int(Wobj.today_temperature_min) < 33:
    tempColor = Alert.FOREGROUND_YELLOW
elif 16 <= int(Wobj.today_temperature_min) < 25:
    tempColor = Alert.FOREGROUND_GREEN
else:
    tempColor = Alert.FOREGROUND_BLUE
AlertObj.Info(
    "Minimum Temperature: {}".format(Wobj.today_temperature_min),
    color=tempColor)
if int(Wobj.today_temperature_max) >= 33:
    tempColor = Alert.FOREGROUND_RED
elif 25 <= int(Wobj.today_temperature_max) < 33:
    tempColor = Alert.FOREGROUND_YELLOW
elif 16 <= int(Wobj.today_temperature_max) < 25:
    tempColor = Alert.FOREGROUND_GREEN
else:
    tempColor = Alert.FOREGROUND_BLUE
AlertObj.Info(
    "Maximum Temperature: {}\n".format(Wobj.today_temperature_max),
    color=tempColor)
AlertObj.Info(
    "Humidity: {}%  Precipitation :{}mm\n\t\t Pressure: {}kPa\n".format(
        Wobj.today_humidity, Wobj.today_precipitation, Wobj.today_presure))
try:
    if int(Wobj.aqi) <= 50:
        tempColor = Alert.FOREGROUND_BLUE
    elif 50 < int(Wobj.aqi) <= 100:
        tempColor = Alert.FOREGROUND_GREEN
    elif 100 < int(Wobj.aqi) <= 150:
        tempColor = Alert.FOREGROUND_YELLOW
    elif 150 < int(Wobj.aqi) <= 200:
        tempColor = Alert.FOREGROUND_RED
    else:
        tempColor = Alert.FOREGROUND_BLACK | Alert.BACKGROUND_DARKRED
except:
    pass
try:
    AlertObj.Info(
        "AQI: \n\t\t Total AQI: {}   pm10: {}   pm2.5 {}\n\t\t AirQuality: {}".
        format(Wobj.aqi, Wobj.pm10, Wobj.pm25, Wobj.qlty))
except:
    try:
        AlertObj.Info(
            "lack some Air Quality data.", color=Alert.FOREGROUND_YELLOW)
        AlertObj.Info(
            "Real time AQI: \n\t\t Total AQI: {}    pm10: {}    pm2.5: {}".
            format(Wobj.aqi, Wobj.pm10, Wobj.pm25),
            color=tempColor)
    except:
        AlertObj.Warn(
            "No avaiable Air Quality data.", color=Alert.BACKGROUND_RED)

AlertObj.Info(
    "============================================================",
    color=Alert.FOREGROUND_WHITE)
AlertObj.Info("Tomorrow: {}".format(Wobj.tomorrow_date))
AlertObj.Info("Condition in day:   {}\n\t\t Condition at night: {}".format(
    Wobj.tomorrow_cond_day, Wobj.tomorrow_cond_night))
if int(Wobj.tomorrow_temperature_min) >= 33:
    tempColor = Alert.FOREGROUND_RED
elif 25 <= int(Wobj.tomorrow_temperature_min) < 33:
    tempColor = Alert.FOREGROUND_YELLOW
elif 16 <= int(Wobj.tomorrow_temperature_min) < 25:
    tempColor = Alert.FOREGROUND_GREEN
else:
    tempColor = Alert.FOREGROUND_BLUE
AlertObj.Info(
    "Minimum Temperature: {}".format(Wobj.tomorrow_temperature_min),
    color=tempColor)
if int(Wobj.tomorrow_temperature_max) >= 33:
    tempColor = Alert.FOREGROUND_RED
elif 25 <= int(Wobj.tomorrow_temperature_max) < 33:
    tempColor = Alert.FOREGROUND_YELLOW
elif 16 <= int(Wobj.tomorrow_temperature_max) < 25:
    tempColor = Alert.FOREGROUND_GREEN
else:
    tempColor = Alert.FOREGROUND_BLUE
AlertObj.Info(
    "Maximum Temperature: {}\n".format(Wobj.tomorrow_temperature_max),
    color=tempColor)
AlertObj.Info("Humidity: {}%  Precipitation :{}mm\n\t\t Pressure: {}kPa\n".
              format(Wobj.tomorrow_humidity, Wobj.tomorrow_precipitation,
                     Wobj.tomorrow_presure))
AlertObj.Info(
    "Update at {} (local)\n\t\t\t   {} (utc)".format(Wobj.updatetime_loc,
                                                     Wobj.updatetime_utc),
    color=Alert.FOREGROUND_WHITE)
AlertObj.Info(
    "============================================================",
    color=Alert.FOREGROUND_WHITE)
shutdown()
# AlertObj.Info("Finish all in {} s".format(time.time() - t0))
# os.system('pause')
