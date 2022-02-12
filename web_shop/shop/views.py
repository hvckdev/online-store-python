from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from web_shop.shop.models import Product, Order


# Create your views here
class ProductListView(generic.ListView):
    model = Product
    template_name = 'shop/product_list.html'


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = 'shop/order_list.html'
