from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, CreateView

from .models import *
from cart.forms import AddCityForm

def city_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    cities = City.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        cities = cities.filter(category=current_category)

    return render(request, 'travel/list.html',
                  {'current_category': current_category, 'categories': categories, 'cities': cities})

def city_detail(request, id, city_slug=None):
    city = get_object_or_404(City, id=id, slug=city_slug)
    add_to_cart = AddCityForm()
    return render(request, 'travel/detail.html', {'city': city, 'add_to_cart':add_to_cart})

