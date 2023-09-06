from django import template


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
