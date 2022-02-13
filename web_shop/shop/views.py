from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django_filters.views import FilterView

from web_shop.shop.filters import ProductFilter
from web_shop.shop.models import Product, Order


# Create your views here
class HomeView(generic.TemplateView):
    template_name = 'shop/home.html'


class ProductListView(FilterView):
    model = Product
    template_name = 'shop/product_list.html'
    filterset_class = ProductFilter


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = 'shop/order_list.html'

    def get_queryset(self):
        return Order.objects.filter(
            user=self.request.user
        )


class CreateOrderView(LoginRequiredMixin, generic.CreateView):
    model = Order
    template_name = 'shop/create_order.html'
    fields = ['size', 'address']
    success_url = reverse_lazy('orders')

    def form_valid(self, form):
        product = Product.objects.get(pk=self.kwargs.get('product_pk'))
        form.instance.user = self.request.user
        form.instance.product = product
        form.instance.tracking_number = 'tracking-number-here'
        form.save()

        product.quantity = product.quantity - 1
        product.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(CreateOrderView, self).get_context_data(**kwargs)
        ctx['product'] = Product.objects.get(pk=self.kwargs.get('product_pk'))
        return ctx
