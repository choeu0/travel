from django.contrib import admin

from travel.models import Category

from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'created', 'updated']
    list_filter = ['created', 'updated', 'category']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = []

admin.site.register(City, CityAdmin)