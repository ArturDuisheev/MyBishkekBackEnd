from django.contrib import admin
from .models import Place, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'avg_price', 'avg_rating',
        'created_by', 'get_categories'
    )
    list_filter = ('avg_rating', 'categories')
    search_fields = ('name', 'description', 'address')
    ordering = ('name',)
    autocomplete_fields = ('categories',)
    raw_id_fields = ('created_by',)

    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    get_categories.short_description = "Категории"
