from django.contrib import admin
from django.urls import path, include

from .helpers.djoser.urls import urlpatterns as djoser_urls
from .swagger import urlpatterns as swagger_urls

api_urlpatterns = [
    path('api/v1/', include('place.urls')),
    path('api/v1/', include('api_solution.urls')),
    path('api/v1/', include(djoser_urls)),
    path('swagger/', include(swagger_urls)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
] + api_urlpatterns
