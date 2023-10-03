from decimal import Decimal
from products.models import Product, ProductVariation


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        if not cart:
            cart = self.session['session_key'] = {}
        self.cart = cart

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        product_variation_ids = self.cart.keys()
        product_variations = ProductVariation.objects.filter(id__in=product_variation_ids)
        cart = self.cart.copy()

        for product in product_variations:
            cart[str(product.id)]['product_variation'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total'] = item['price'] * item['quantity']
            yield item

    def add(self, product_variation, quantity):
        product_id = str(product_variation.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'product_id': product_variation.product.name, 'quantity': quantity, 'price': str(
                product_variation.product.price)}
        self.cart[product_id]['quantity'] = quantity
        self.session.modified = True

    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True

    def update(self, product, quantity):
        product_id = str(product)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] = quantity
            self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
