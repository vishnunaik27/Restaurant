from django.contrib import admin
from .models import Product, Order

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available')
    list_filter = ('available',)
    search_fields = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ( 'customer_name', 'product', 'quantity', 'order_time')
    list_filter = ('order_time',)

