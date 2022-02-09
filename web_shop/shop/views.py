from django.shortcuts import render
from django.views import generic
from web_shop.shop.models import Product


# Create your views here
class ProductListView(generic.ListView):
    model = Product
    template_name = 'shop/index.html'
