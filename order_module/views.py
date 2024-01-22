from django.shortcuts import render
from .models import *


# Create your views here.
def add_product_to_cart(request, id):
    books = Book.objects.all()
    if request.user.is_authenticated:
        current_order, created = Order.objects.get_or_create(user_id=request.user.id, is_paid=False)
        current_order_detail = current_order.orderdetail_set.filter(product_id=id).first()

        if current_order_detail is not None:
            current_order_detail.save()
        else:
            new_detail = OrderDetail(order_id=current_order.id, product_id=id)
            new_detail.save()
        return render(request, 'book_list.html', context={
            'books': books
        })

def show_cart(request):
    products = OrderDetail.objects.filter(order__user_id=request.user.id, order__is_paid=False).all()
    return render(request, 'cart.html', context={
        'cart': products
    })

def payment(request):
    order: Order = Order.objects.filter(user_id=request.user.id, is_paid=False).first()
    order.is_paid = True
    order.save()
    return render(request, 'cart.html', {

    })

def my_history(request):
    orders = Order.objects.filter(user_id=request.user.id, is_paid=True).all()
    return render(request, 'history.html', context={
        'orders': orders
    })