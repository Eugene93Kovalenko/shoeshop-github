from .cart import Cart


def cart(request):
    return {'cart': list(Cart(request))}
