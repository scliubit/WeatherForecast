from Alert import Alert
alt = Alert()


class WeatherInfo(object):
    def __init__(self, weather_dict):
        if __name__ == '__main__':
            print("WeatherInfo constructing...")
        alt.Info("Constructing Weather Info Module")
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
        self.today_temperature_max = self.daily[1]['tmp'][
            'max']  # Degree Celsius
        # aqi
        try:
            self.pm10 = self._aqi['city']['pm10']
            self.pm25 = self._aqi['city']['pm25']
            self._aqi = WeatherData['aqi']
            self.aqi = self._aqi['city']['aqi']
            self.co = self._aqi['city']['co']
            self.no2 = self._aqi['city']['no2']
            self.o3 = self._aqi['city']['o3']
            self.so2 = self._aqi['city']['so2']
            self.qlty = self._aqi['city']['qlty']
        except:
            alt.Warn("Some Information did not found.")
        # basic information
        self.basic = WeatherData['basic']
        self.updatetime_loc = self.basic['update']['loc']
        self.updatetime_utc = self.basic['update']['utc']
        self.latitude = self.basic['lat']
        self.longitude = self.basic['lon']
