from django.contrib import admin
from .models import Product, Order, OrderItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category']
    search_fields = ['name', 'category']

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product_name', 'price', 'quantity']
    can_delete = False

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'address', 'total_price_display', 'product_list_display', 'created_at']
    inlines = [OrderItemInline]
    readonly_fields = ['name', 'email', 'address', 'phone', 'total_price', 'created_at']

    def total_price_display(self, obj):
        return f"₹{obj.total_price:.2f}"
    total_price_display.short_description = 'Total Price'

    def product_list_display(self, obj):
        products = [f"{item.product_name} (x{item.quantity})" for item in obj.orderitem_set.all()]
        return ", ".join(products) if products else "No items"
    product_list_display.short_description = 'Products Ordered'
