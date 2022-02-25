import django_filters

from web_shop.shop.models import Product


class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__name')

    class Meta:
        model = Product
        fields = ['category']
в