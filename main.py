import json
import time
import os
import socket
import re
from Alert import Alert as Alt
import Alert
from urllib import request
from urllib.parse import quote
AlertObj = Alt()
runtime = time.time()


# analyze weather information
class WeatherInfo(object):
    def __init__(self, weather_dict):
        if __name__ == '__main__':
            AlertObj.Info(
                "Constructing Weather Info Module",
                color=Alert.FOREGROUND_WHITE)
        if weather_dict['HeWeather5'][0]['status'] == 'ok':
            pass
        else:
            AlertObj.Warn("Unable to get Weather Data!")
            shutdown()
        WeatherData = weather_dict['HeWeather5']
        WeatherData = WeatherData[0]
        # print(WeatherData)
        # daily_forecast
        self.daily = WeatherData['daily_forecast']
        # today
        self.today_moonrise = self.daily[0]['astro']['mr']
        self.today_moonset = self.daily[0]['astro']['ms']
        self.today_sunrise = self.daily[0]['astro']['sr']
        self.today_sunset = self.daily[0]['astro']['ss']
        self.today_cond_day = self.daily[0]['cond']['txt_d']
        self.today_cond_night = self.daily[0]['cond']['txt_n']
        self.today_humidity = self.daily[0]['hum']  # percentage
        self.today_precipitation = self.daily[0]['pcpn']  # millimeter
        self.today_rainy_percentage = self.daily[0]['pop']  # percentage
        self.today_presure = float(self.daily[0]['pres']) / 10  # kPa
        self.today_temperature_min = self.daily[0]['tmp'][
            'min']  # Degree Celsius
        self.today_temperature_max = self.daily[0]['tmp'][
            'max']  # Degree Celsius
        self.today_uv = self.daily[0]['uv']
        self.today_visibility = self.daily[0]['vis']
        self.today_wind = self.daily[0]['wind']
        self.today_wind_deg = self.today_wind['deg']
        self.today_wind_dir = self.today_wind['dir']
        self.today_wind_power = self.today_wind['sc']
        self.today_wind_windspeed = self.today_wind['spd']  # kmph
        # tomorrow
        self.tomorrow_moonrise = self.daily[1]['astro']['mr']
        self.tomorrow_moonset = self.daily[1]['astro']['ms']
        self.tomorrow_sunrise = self.daily[1]['astro']['sr']
        self.tomorrow_sunset = self.daily[1]['astro']['ss']
        self.tomorrow_cond_day = self.daily[1]['cond']['txt_d']
        self.tomorrow_cond_night = self.daily[1]['cond']['txt_n']
        self.tomorrow_humidity = self.daily[1]['hum']  # percentage
        self.tomorrow_precipitation = self.daily[1]['pcpn']  # millimeter
        self.tomorrow_rainy_percentage = self.daily[1]['pop']  # percentage
        self.tomorrow_presure = float(self.daily[1]['pres']) / 10  # kPa
        self.tomorrow_temperature_min = self.daily[1]['tmp'][
            'min']  # Degree Celsius
        self.tomorrow_temperature_max = self.daily[1]['tmp'][
            'max']  # Degree Celsius
        self.tomorrow_uv = self.daily[1]['uv']
        self.tomorrow_visibility = self.daily[1]['vis']
        self.tomorrow_wind = self.daily[1]['wind']
        self.tomorrow_wind_deg = self.tomorrow_wind['deg']
        self.tomorrow_wind_dir = self.tomorrow_wind['dir']
        self.tomorrow_wind_power = self.tomorrow_wind['sc']
        self.tomorrow_wind_windspeed = self.tomorrow_wind['spd']  # kmph
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
            AlertObj.Warn("Some Information did not found in aqi section.")
        # basic information
        self.basic = WeatherData['basic']
        self.updatetime_loc = self.basic['update']['loc']
        self.updatetime_utc = self.basic['update']['utc']
        self.latitude = self.basic['lat']
        self.longitude = self.basic['lon']
        # now
        self.now = WeatherData['now']
        self.now_cond = self.now['cond']['txt']
        self.now_feel = self.now['fl']  # sendible temperature
        self.now_temperature = self.now['tmp']
        self.now_humidity = self.now['hum']  # percentage
        self.now_precipitation = self.now['pcpn']  # millimeter
        self.now_presure = float(self.now['pres']) / 10  # kPa
        AlertObj.Info(
            "Finish analyzing weather data", color=Alert.FOREGROUND_WHITE)


def shutdown():
    '''shut down'''
    AlertObj.Info(
        "Finish all in {} s".format(time.time() - runtime),
        color=Alert.FOREGROUND_WHITE)
    os.system('pause')
    exit()


# For IP address
ip_url = "http://www.ipip.net"
with request.urlopen(ip_url) as urlf:
    urlstring = urlf.read()
    ip = re.findall(b'\d+\.\d+\.\d+\.\d+', urlstring)[1]
    ipstring = ip.decode()
    if ipstring == '':
        AlertObj.Warn("Fail to get your IPv4 - Address")
hostname = socket.gethostname()
AlertObj.Info("Hello %s user." % hostname, color=Alert.FOREGROUND_WHITE)
AlertObj.Info("Your IPv4 Address:    {}".format(ipstring))

now = time.time()

url = "https://www.ipip.net/ip.html"
string = request.urlopen(url).read()
xre = b'(<div style="text-align: center;color:red;font-size: 20px;font-weight: 600;">)(.+)(</div>)'
z = re.search(xre, string).group(2).decode()
location = z.split(" ")
city = location[-1]
# finish
key = ''  # BUY A KEY BY YOURSELF
if key == '':
    print('No available key')
    exit()
url = "https://free-api.heweather.com/v5/weather?city=" + quote(
    city) + "&key=" + key

content = request.urlopen(url).read()
data = json.loads(content.decode())

wobj = WeatherInfo(data)
tmpColor = Alert.FOREGROUND_WHITE
if float(wobj.latitude) >= 0:
    lat = 'N'
else:
    lat = 'S'
if float(wobj.longitude) >= 0:
    lon = 'E'
else:
    lon = 'W'
AlertObj.Info(
    "============================================================",
    color=Alert.FOREGROUND_WHITE)
AlertObj.Info("Weather Forecast for {}".format(city))
AlertObj.Info(
    "latitude:      {}°{}\n\t\t longitude:     {}°{}".format(
        wobj.latitude, lat, wobj.longitude, lon),
    color=Alert.FOREGROUND_WHITE)
if int(wobj.now_temperature) >= 33 or int(wobj.now_feel) >= 33:
    tempColor = Alert.FOREGROUND_RED
elif 25 <= int(wobj.now_temperature) < 33 and 25 <= int(wobj.now_feel) < 33:
    tempColor = Alert.FOREGROUND_YELLOW
elif 16 < int(wobj.now_temperature) < 25 and 16 < int(wobj.now_feel) < 25:
    tempColor = Alert.FOREGROUND_GREEN
else:
    pass
AlertObj.Info(
    "Real Time Weather: \n\t\t Condition: {}    Temperature: {}℃\n\t\t Sendible Temperature: {}℃".
    format(wobj.now_cond, wobj.now_temperature, wobj.now_feel),
    color=tempColor)
if int(wobj.today_temperature_min) >= 33:
    tempColor = Alert.FOREGROUND_RED
elif 25 <= int(wobj.today_temperature_min) < 33:
    tempColor = Alert.FOREGROUND_YELLOW
elif 16 <= int(wobj.today_temperature_min) < 25:
    tempColor = Alert.FOREGROUND_GREEN
else:
    tempColor = Alert.FOREGROUND_BLUE
AlertObj.Info(
    "Minimum Temperature: {}".format(wobj.today_temperature_min),
    color=tempColor)
if int(wobj.today_temperature_max) >= 33:
    tempColor = Alert.FOREGROUND_RED
elif 25 <= int(wobj.today_temperature_max) < 33:
    tempColor = Alert.FOREGROUND_YELLOW
elif 16 <= int(wobj.today_temperature_max) < 25:
    tempColor = Alert.FOREGROUND_GREEN
else:
    tempColor = Alert.FOREGROUND_BLUE
AlertObj.Info(
    "Maximum Temperature: {}".format(wobj.today_temperature_max),
    color=tempColor)
AlertObj.Info(
    "Update at {} (local)\n\t\t\t   {} (utc)".format(wobj.updatetime_loc,
                                                     wobj.updatetime_utc),
    color=Alert.FOREGROUND_WHITE)
try:
    if int(wobj.aqi) <= 50:
        tempColor = Alert.FOREGROUND_BLUE
    elif 50 < int(wobj.aqi) <= 100:
        tempColor = Alert.FOREGROUND_GREEN
    elif 100 < int(wobj.aqi) <= 150:
        tempColor = Alert.FOREGROUND_YELLOW
    elif 150 < int(wobj.aqi) <= 200:
        tempColor = Alert.FOREGROUND_RED
    else:
        tempColor = Alert.FOREGROUND_BLACK | Alert.BACKGROUND_DARKRED
except:
    pass
try:
    AlertObj.Info(
        "Real time AQI: \n\t\t Total AQI: {}    pm10: {}    pm2.5 {}\n\t\t AirQuality: {}".
        format(wobj.aqi, wobj.pm10, wobj.pm25, wobj.qlty))
except:
    try:
        AlertObj.Info(
            "lack some Air Quality data.", color=Alert.FOREGROUND_YELLOW)
        AlertObj.Info(
            "Real time AQI: \n\t\t Total AQI: {}    pm10: {}    pm2.5: {}".
            format(wobj.aqi, wobj.pm10, wobj.pm25),
            color=tempColor)
    except:
        AlertObj.Warn(
            "No avaiable Air Quality data.", color=Alert.BACKGROUND_RED)

AlertObj.Info(
    "============================================================",
    color=Alert.FOREGROUND_WHITE)
shutdown()
AlertObj.Info("Finish all in {} s".format(time.time() - runtime))
os.system('pause')
