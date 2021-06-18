from django.contrib import admin
from news.models import CategoriesModel, ArticleModel


@admin.register(CategoriesModel)
class CategoriesModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(ArticleModel)
class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ['headline', 'content', 'created_at', 'source']
    list_filter = ['headline', 'created_at']
    search_fields = ['headline', 'created_at', 'source', 'categories']
