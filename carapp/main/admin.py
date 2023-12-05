from django.contrib import admin
from main.models import AppInfo, Category, Product  # instead of importing all the model class created, wildcard * can be use for all
# e.g from main.models import * instead of from main.models import AppInfo, Category, Product

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('Brand',)}  # note class category return brand in model file
    list_display = ['id', 'Brand']
    search_fields = ['id', 'Brand']


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('model',)}  # note class product return model in model file
    list_display = ['id', 'type', 'model', 'year', 'seats', 'price', 'promo_price', 'uploaded_at', 'color', 'Register']
    search_fields = ['id', 'type', 'model', 'year', 'seats', 'price', 'promo_price', 'uploaded_at']
admin.site.register(AppInfo)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
