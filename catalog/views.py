import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Product, Order, OrderItem
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

def home(request):
    return render(request, 'catalog/home.html')

# Product list view
def product_list(request):
    categories = Product.objects.values_list('category', flat=True).distinct()  # Get all unique categories
    selected_category = request.GET.get('category', '')  # Get selected category from query params
    query = request.GET.get("q", "")  # Get search query

    # Show all products initially
    products = Product.objects.all()

    # Filter by selected category if provided
    if selected_category:
        products = products.filter(category=selected_category)

    # Apply search filter if query exists
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
    return render(request, 'catalog/cart.html', {
        'cart': cart,
        'MEDIA_URL': settings.MEDIA_URL  # Correctly pass this as part of the context
    })

# Checkout view
def checkout(request):
    cart = request.session.get('cart', [])  # Comes from localStorage via JavaScript, or saved manually earlier
    delivery_fee = 50
    total_price = sum(item['price'] * item['quantity'] for item in cart)
    grand_total = total_price + delivery_fee

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST.get('phone', '')

        # Save order
        order = Order.objects.create(
            name=name,
            email=email,
            address=address,
            total_price=grand_total
        )

        # Save each cart item
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product_name=item['name'],
                price=item['price'],
                quantity=item['quantity']
            )

        request.session['cart'] = []

        return redirect('order_confirm')  # Redirect to confirmation

    return render(request, 'catalog/checkout.html', {
        'cart': cart,
        'total_price': total_price,
        'delivery_fee': delivery_fee,
        'grand_total': grand_total
    })
    
def save_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        request.session['cart'] = data.get('cart', [])
        return JsonResponse({'status': 'success'})


def send_order_confirmation_email(order):
    # Get the order details
    name = order.name
    email = order.email
    address = order.address
    total_price = order.total_price
    
    # Prepare the context for the email template
    context = {
        'name': name,
        'email': email,
        'address': address,
        'total_price': total_price
    }

    # Render the email HTML with context
    email_body = render_to_string('order_confirm.html', context)
    
    # Send the email
    send_mail(
        'Order Confirmed - Your Order has been Placed Successfully!',
        'Please see the attached confirmation for your order.',
        settings.DEFAULT_FROM_EMAIL,  # Sender's email
        [email],  # Receiver's email (customer)
        fail_silently=False,
        html_message=email_body  # HTML version of the email
    )
# Order confirmation
def order_confirm(request):
    return render(request, 'catalog/order_confirm.html')
