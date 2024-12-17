from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','item_name', 'new_price','discount')
    search_fields = ('new_price',)  # 
    list_filter = ('item_name',)
