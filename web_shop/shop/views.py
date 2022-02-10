from django.shortcuts import render
from django.views import generic
from web_shop.shop.models import Product, Order


# Create your views here
class ProductListView(generic.ListView):
    model = Product
    template_name = 'shop/product_list.html'


class OrderListView(generic.ListView):
    model = Order
    template_name = 'shop/order_list.html'
