from django.db import models
from account_module.models import User
from product_module.models import Book
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField()
    def __str__(self):
        return str(self.id)

class OrderDetail(models.Model):
        order = models.ForeignKey(Order, on_delete=models.CASCADE)
        product = models.ForeignKey(Book, on_delete=models.CASCADE)

        def __str__(self):
            return str(self.order)