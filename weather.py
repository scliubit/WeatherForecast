from Alert import Alert
alt = Alert()


class WeatherInfo(object):
    def __init__(self, weather_dict):
        if __name__ == '__main__':
            print("WeatherInfo constructing...")
        alt.Info("Constructing Weather Info Module")
        try:
            if weather_dict['HeWeather5'][0]['status'] == 'ok':
                pass
        except:
            alt.Warn("Unable to get Weather Data!")
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
            alt.Warn("Some Information did not found in aqi section.")
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
        self.now_humidity = self.now['hum']  # percentage
        self.now_precipitation = self.now['pcpn']  # millimeter
        self.now_presure = float(self.now['pres']) / 10  # kPa
