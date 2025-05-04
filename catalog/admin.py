from django.contrib import admin
from .models import Product, Order, OrderItem

admin.site.register(Product)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product_name', 'price', 'quantity']
    can_delete = False

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'address', 'total_price_display', 'product_list_display', 'created_at']
    inlines = [OrderItemInline]
    readonly_fields = ['total_price', 'created_at']

    def total_price_display(self, obj):
        # Ensure the total price is correctly formatted
        return f"₹{obj.total_price:.2f}"
    total_price_display.short_description = 'Total Price'

    def product_list_display(self, obj):
        # Ensure products are correctly fetched from the related order items
        products = [item.product_name for item in obj.orderitem_set.all()]
        return ", ".join(products) if products else "No items"
    product_list_display.short_description = 'Product List'