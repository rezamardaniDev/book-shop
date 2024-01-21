from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    GENDER_CHOISE = (
        ('M', 'male'),
        ('F', 'female'),
    )
    phone_number = models.CharField(max_length=11, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOISE, default='M')
    date_of_birth = models.DateField()
    state = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=250, null=True)
    city_address = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'