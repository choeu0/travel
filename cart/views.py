from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from travel.models import City

from .forms import AddCityForm
from .cart import Cart


@require_POST

def add(request, city_id):
    cart = Cart(request)
    city = get_object_or_404(City, id=city_id)
    form = AddCityForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(city=city, is_update=cd['is_update'])
    return redirect('cart:detail')

def remove(request, city_id):
    cart = Cart(request)
    city = get_object_or_404(City, id=city_id)
    cart.remove(city)
    return redirect('cart:detail')

def detail(request):
    cart = Cart(request)
    for city in cart:
        city['quantity_form'] = AddCityForm(initial={'is_update':True})
        return render(request, 'cart/detail.html', {'cart':cart})