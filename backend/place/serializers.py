from rest_framework import serializers
from .models import Place, Category, PlaceImage


class PlaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceImage
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class PlaceSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    place_images = PlaceImageSerializer(many=True, read_only=True)
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Place
        fields = [
            'id', 'name', 'avg_price', 'avg_rating',
            'coordinates_x', 'coordinates_y', 'description',
            'phone', 'whatsapp', 'instagram', 'address', 'place_images',
            'categories', 'created_by'
        ]
