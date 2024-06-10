from django.contrib import admin
from apps.search import models as search_models


# Register your models here.
@admin.register(search_models.SearchLog)
class SearchAdmin(admin.ModelAdmin):
    list_filter = ['user', 'query']
    search_fields = ['user', 'query']
    list_display = ['user', 'query']
