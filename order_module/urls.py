from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('add_to_cart/<id>', views.add_product_to_cart, name='add_to_cart'),
    path('show-cart', views.show_cart, name='show_cart'),
    path('payment', views.payment, name='payment'),
    path('history', views.my_history, name='my_history')
]