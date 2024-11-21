from django.contrib import admin
from django.urls import path, include

from .helpers.djoser.urls import urlpatterns as djoser_urls
from .swagger import urlpatterns as swagger_urls

api_urlpatterns = [
    path('place/', include('place.urls')),
    path('api_solution/', include('api_solution.urls')),
    path('auth/', include(djoser_urls)),
    path('swagger/', include(swagger_urls)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urlpatterns))
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)