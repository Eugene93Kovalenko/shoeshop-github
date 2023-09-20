from django import template

from orders.models import OrderItem

register = template.Library()

# для того, чтобы пагинация работала при сортировке
@register.simple_tag()
def relative_url(argument, value, urlencode=None):
    url = f'?{argument}={value}'
    if urlencode.count('=') == 1 and urlencode.startswith('page'):
        return url
    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = querystring[1:] if querystring[0].startswith('page') else querystring
        encoded_querystring = '&'.join(filtered_querystring)
        url = f'{url}&{encoded_querystring}'
    return url


# перенести во views
@register.simple_tag
def get_path_for_breadcrumbs(url):
    path = f'{url[1:-1]}'
    return path


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
# def query_transform(context, **kwargs):
#     '''
#     Returns the URL-encoded querystring for the current page,
#     updating the params with the key/value pairs passed to the tag.
#
#     E.g: given the querystring ?foo=1&bar=2
#     {% query_transform bar=3 %} outputs ?foo=1&bar=3
#     {% query_transform foo='baz' %} outputs ?foo=baz&bar=2
#     {% query_transform foo='one' bar='two' baz=99 %} outputs ?foo=one&bar=two&baz=99
#
#     A RequestContext is required for access to the current querystring.
#     '''
#     query = context['request'].GET.copy()
#     for k, v in kwargs.items():
#         query[k] = v
#     for k in [k for k, v in query.items() if not v]:
#         del query[k]
#     return query.urlencode()


# @register.simple_tag(takes_context=True)
# def param_replace(context, **kwargs):
#     d = context['request'].GET.copy()
#     for k, v in kwargs.items():
#         d[k] = v
#     for k in [k for k, v in d.items() if not v]:
#         del d[k]
#     return d.urlencode()
