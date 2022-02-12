import random

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

    def get_queryset(self):
        return Order.objects.filter(
            user=self.request.user
        )


class CreateOrderView(generic.CreateView):
    model = Order
    template_name = 'shop/create_order.html'
    fields = ['address']
    success_url = '/orders'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.product = Product.objects.get(pk=self.kwargs.get('product_pk'))
        form.instance.tracking_number = 'tracking-number-here'
        form.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(CreateOrderView, self).get_context_data(**kwargs)
        ctx['product'] = Product.objects.get(pk=self.kwargs.get('product_pk'))
        return ctx
