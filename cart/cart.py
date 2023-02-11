from products.models import Product


class Cart:
    def __int__(self, request):
        """
        Initialize The Cart
       """
        self.request = request
        self.session = request.session
        cart = self.session.get('card')
        if not cart:
            cart = self.session['card'] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        """
         Add thr specified Product to the cart if it exists
        """
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id] = {'quantity': quantity}

        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    def save(self):
        """
          Mark Session as  modified To Save Changes
        """
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            product = cart[str(product.id)]['product_obj']
        for item in cart.values():
            yield item

    def __len(self):
        return len(self.cart.keys())

    def clear(self):
        del self.cart.session['cart']
        self.save()

    def get_total_price(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return sum(product.price for product in products)
