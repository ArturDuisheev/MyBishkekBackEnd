from django_filters import rest_framework as filters
from .models import Place

class PlaceFilter(filters.FilterSet):
    rating = filters.NumberFilter(field_name="avg_rating", lookup_expr="gte")
    min_price = filters.NumberFilter(field_name="avg_price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="avg_price", lookup_expr="lte")
    category = filters.BaseInFilter(field_name="categories__id", lookup_expr="in")

    class Meta:
        model = Place
        fields = ['rating', 'min_price', 'max_price', 'category']
