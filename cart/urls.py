from django.urls import path

from .views import *

app_name = 'cart'

urlpatterns = [
    path('detail/', detail, name='detail'),
    path('add/<int:city_id>', add, name='city_add'),
    path('remove/<city_id>', remove, name='city_remove'),
]