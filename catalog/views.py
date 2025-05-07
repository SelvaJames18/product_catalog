import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Product, Order, OrderItem
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

def home(request):
    return render(request, 'catalog/home.html')

def product_list(request):
    categories = Product.objects.values_list('category', flat=True).distinct()
    selected_category = request.GET.get('category', '')
    query = request.GET.get('q', '')
    products = Product.objects.all()

    if selected_category:
        products = products.filter(category=selected_category)
    if query:
        products = products.filter(name__icontains=query)

    return render(request, 'catalog/product_list.html', {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
        'query': query,
    })

def cart_view(request):
    cart = request.session.get('cart', [])
    return render(request, 'catalog/cart.html', {
        'cart': cart,
        'MEDIA_URL': settings.MEDIA_URL
    })

def checkout(request):
    cart = request.session.get('cart', [])
    delivery_fee = 50
    total_price = sum(item['price'] * item['quantity'] for item in cart)
    grand_total = total_price + delivery_fee

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST.get('phone', '')

        order = Order.objects.create(
            name=name,
            email=email,
            address=address,
            total_price=grand_total,
            phone=phone
        )

        for item in cart:
            OrderItem.objects.create(
                order=order,
                product_name=item['name'],
                price=item['price'],
                quantity=item['quantity']
            )

        # Optional: send order confirmation email
        # send_order_confirmation_email(order)

        request.session['cart'] = []

        return redirect('order_confirm')

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
    context = {
        'name': order.name,
        'email': order.email,
        'address': order.address,
        'total_price': order.total_price,
        'phone': order.phone,
    }
    email_body = render_to_string('order_confirm.html', context)
    send_mail(
        'Order Confirmed - Your Order has been Placed Successfully!',
        'Please see the attached confirmation for your order.',
        settings.DEFAULT_FROM_EMAIL,
        [order.email],
        fail_silently=False,
        html_message=email_body
    )

def order_confirm(request):
    return render(request, 'catalog/order_confirm.html')
