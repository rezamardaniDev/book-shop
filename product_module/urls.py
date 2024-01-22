from django.urls import path
from . import views
app_name = 'product'

urlpatterns = [
    path('books', views.book_list, name='books')
]