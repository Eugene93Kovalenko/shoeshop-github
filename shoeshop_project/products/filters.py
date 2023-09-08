import django_filters

from products.models import Product


class ProductFilter(django_filters.FilterSet):
    brand__name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Product
        fields = ['brand']
