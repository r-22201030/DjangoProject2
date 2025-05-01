

from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)

admin.site.register(Product, ProductAdmin)

# shop/admin.py
from django.contrib import admin
from .models import Category, Item

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active')

admin.site.register(Category, CategoryAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available')

admin.site.register(Item, ItemAdmin)

