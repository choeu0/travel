# from decimal import Decimal
from django.conf import settings
from travel.models import City


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_ID)
        if not cart:
            cart = self.session[settings.CART_ID] = {}
        self.cart = cart

    # def __len__(self):
    #     return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        city_ids = self.cart.keys()

        cities = City.objects.filter(id__in=city_ids)

        for city in cities:
            self.cart[str(city.id)]['city'] = city

        for item in self.cart.values():
            yield item


    def add(self, city, quantity=1, is_update=False):
        city_id = str(city.id)
        if city_id not in self.cart:
            self.cart[city_id] = {'quantity':0}

        if is_update:
            self.cart[city_id]['quantity'] = quantity
        else:
            self.cart[city_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session[settings.CART_ID] = self.cart
        self.session.modified = True

    def remove(self, city):
        city_id = str(city.id)
        if city_id in self.cart:
            del(self.cart[city_id])
            self.save()

