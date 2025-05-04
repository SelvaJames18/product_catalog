from django.shortcuts import render, redirect
from .models import Product, Order, OrderItem
from django.core.mail import send_mail
from django.conf import settings

# Product list view
def product_list(request):
    categories = Product.objects.values_list('category', flat=True).distinct()  # Get unique categories
    selected_category = request.GET.get('category', '')  # Get selected category from URL parameters
    query = request.GET.get("q", "")  # Get search query from URL parameters

    if selected_category:
        products = Product.objects.filter(category=selected_category)
    else:
        products = Product.objects.all()  

    if query:
        products = products.filter(name__icontains=query)

    return render(request, 'catalog/product_list.html', {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
        'query': query,
    })
# Cart view
def cart_view(request):
    cart = request.session.get('cart', [])
    return render(request, 'catalog/cart.html', {'cart': cart})

# Checkout view
def checkout(request):
    cart = request.session.get('cart', [])
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']

        # Calculate total price
        total_price = sum(item['price'] * item['quantity'] for item in cart)

        # Create Order
        order = Order.objects.create(
            name=name,
            email=email,
            address=address,
            total_price=total_price
        )

        # Create OrderItems
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product_name=item['name'],  # If using ForeignKey, use product=product_instance
                price=item['price'],
                quantity=item['quantity']
            )

        # Clear cart
        request.session['cart'] = []

        # Optional: Send confirmation email
        # send_mail(...)

        return redirect('order_confirm')

    return render(request, 'catalog/checkout.html', {'cart': cart})

# Order confirmation
def order_confirm(request):
    return render(request, 'catalog/order_confirm.html')
