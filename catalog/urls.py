from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('products/', views.product_list, name='product_list'),  # Product listing
    path('cart/', views.cart_view, name='cart'),  # Cart page
    path('save-cart/', views.save_cart, name='save_cart'),
    path('checkout/', views.checkout, name='checkout'),  # Checkout page
    path('order-confirm/', views.order_confirm, name='order_confirm'), 

]
