from django.contrib import admin
from .models import Product, Order,Customer,Payment,Review

# Online Website, selling: socks and mugs
admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'description')


admin.site.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'created_at', 'total_price')


admin.site.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')



admin.site.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'amount', 'created_at','payment_method')



admin.site.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'rating', 'comment', 'created_at')



