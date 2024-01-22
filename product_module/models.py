from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Publisher(models.Model):
    name = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    inventory = models.CharField(max_length=255, null=True)
    price = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title