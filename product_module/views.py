from django.shortcuts import render
from .models import *
# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', context={
        'books': books
    })