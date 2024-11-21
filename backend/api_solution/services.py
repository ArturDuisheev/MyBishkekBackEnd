import requests


class WeatherService:
    IP_API_URL = 'http://ip-api.com/json/'
    WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"
    API_KEY = "8ed6c0f2b978147e0b139b888ea46349"

    @staticmethod
    def get_coordinates_by_ip(ip=None):
        """
        Получить координаты (широту и долготу) по IP.
        """
        try:
            response = requests.get(f"{WeatherService.IP_API_URL}{ip or ''}")
            if response.status_code == 200:
                data = response.json()
                if data["status"] == "success":
                    return data["lat"], data["lon"]
                else:
                    raise ValueError(f"Ошибка в ответе API геолокации: {data}")
            else:
                raise ConnectionError(f"Ошибка подключения к API геолокации: {response.status_code}")
        except Exception as e:
            raise RuntimeError(f"Ошибка при запросе геолокации: {str(e)}")

    @staticmethod
    def get_weather(lat, lon):
        """
        Получить текущую погоду по координатам.
        """
        params = {
            "lat": lat,
            "lon": lon,
            "appid": WeatherService.API_KEY,
            "units": "metric",  # Для получения температуры в Цельсиях
            "lang": "ru"  # Для получения ответа на русском языке
        }

        try:
            response = requests.get(WeatherService.WEATHER_API_URL, params=params)
            if response.status_code == 200:
                return response.json()
            else:
                raise ConnectionError(f"Ошибка подключения к API погоды: {response.status_code, response.text}")
        except Exception as e:
            raise RuntimeError(f"Ошибка при запросе погоды: {str(e)}")


import requests


class AirQualityService:
    IP_API_URL = 'http://ip-api.com/json/'
    AIR_QUALITY_API_URL = "http://api.openweathermap.org/data/2.5/air_pollution"
    API_KEY = "8ed6c0f2b978147e0b139b888ea46349"

    @staticmethod
    def get_coordinates_by_ip(ip=None):
        try:
            response = requests.get(f"{AirQualityService.IP_API_URL}{ip or ''}")
            if response.status_code == 200:
                data = response.json()
                if data["status"] == "success":
                    return data["lat"], data["lon"]
                else:
                    raise ValueError(f"Ошибка в ответе API геолокации: {data}")
            else:
                raise ConnectionError(f"Ошибка подключения к API геолокации: {response.status_code}")
        except Exception as e:
            raise RuntimeError(f"Ошибка при запросе геолокации: {str(e)}")

    @staticmethod
    def get_air_quality(lat, lon):
        params = {
            "lat": lat,
            "lon": lon,
            "appid": AirQualityService.API_KEY,
        }

        try:
            response = requests.get(AirQualityService.AIR_QUALITY_API_URL, params=params)
            if response.status_code == 200:
                return response.json()
            else:
                raise ConnectionError(f"Ошибка подключения к API качества воздуха: {response.status_code}")
        except Exception as e:
            raise RuntimeError(f"Ошибка при запросе качества воздуха: {str(e)}")
