from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # Product list page
    path('cart/', views.cart_view, name='cart'),  # Cart page
    path('checkout/', views.checkout, name='checkout'),  # Checkout page
    path('order_confirm/', views.order_confirm, name='order_confirm'),  # Order confirmation page
]
