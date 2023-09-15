from django import template

from orders.models import OrderItem

register = template.Library()


@register.simple_tag
def relative_url(page, value, urlencode=None):
    url = f'?{page}={value}'
    if urlencode.count('=') == 1 and urlencode.startswith('page'):
        return url
    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = querystring[1:] if querystring[0].startswith('page') else querystring
        encoded_querystring = '&'.join(filtered_querystring)
        url = f'{url}&{encoded_querystring}'
    return url


@register.simple_tag
def get_path_for_breadcrumbs(url):
    path = f'{url[1:-1]}'
    return path


@register.simple_tag
def get_total_discount():
    total = 0
    for item in OrderItem.objects.all():
        total += item.product_variation.product.price * item.quantity - item.product_variation.product.discount_price * item.quantity
    return total


@register.simple_tag
def get_total_all_products_price():
    total = 0
    for item in OrderItem.objects.all():
        total += item.get_total_product_price()
    return total



# @register.simple_tag
# def relative_url(field_name, value, urlencode=None):
#     url = f'?{field_name}={value}'
#     if urlencode.count('=') > 1:
#         if urlencode.startswith('page'):
#             en = urlencode[urlencode.find('&')+1:]
#             print('-'+en)
#         querystring = urlencode.split('&')
#         # filtered_querystring = filter(lambda p: p.split('=')[0] != field_name, querystring)
#         filtered_querystring = querystring[1:] if querystring[0].startswith('page') else querystring
#         encoded_querystring = '&'.join(filtered_querystring)
#         print(encoded_querystring)
#         url = f'{url}&{encoded_querystring}'
#     return url


# @register.simple_tag(takes_context=True)
# def pagination_url(context, *args, **kwargs):
#     query = context['request'].GET.copy()
#     for k, v in kwargs.items():
#         query[k] = v
#     return query.urlencode()
