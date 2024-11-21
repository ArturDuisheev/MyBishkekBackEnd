from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import WeatherService, AirQualityService


class WeatherView(APIView):
    """
    Представление для получения текущей погоды по IP адресу.
    """

    def get(self, request, *args, **kwargs):
        ip = request.GET.get('ip', None)  # Если нужно явно указать IP
        try:
            # Получаем координаты по IP
            lat, lon = WeatherService.get_coordinates_by_ip(ip)

            # Получаем текущую погоду
            weather_data = WeatherService.get_weather(lat, lon)

            return Response(weather_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AirQualityView(APIView):

    def get(self, request, *args, **kwargs):
        ip = request.GET.get('ip', None)
        try:
            lat, lon = AirQualityService.get_coordinates_by_ip(ip)

            air_quality_data = AirQualityService.get_air_quality(lat, lon)

            return Response(air_quality_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
