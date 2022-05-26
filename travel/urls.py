from django.urls import path
from .views import *

app_name = 'travel'

urlpatterns = [
    path('', city_in_category, name='city_all'),
    path('<slug:category_slug>/', city_in_category, name='city_in_category'),
    path('<int:id>/<city_slug>/', city_detail, name='city_detail'),
    
    # path('/<int:pk>/', DetailCityView.as_view(), name='city_detail'),
]


