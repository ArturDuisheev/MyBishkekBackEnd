from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Place, Category
from .serializers import PlaceSerializer, CategorySerializer
from .filters import PlaceFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PlaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PlaceFilter
    permission_classes = [IsAuthenticatedOrReadOnly]
