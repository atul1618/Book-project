from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_name=models.CharField(max_length=120)
    email=models.EmailField(max_length=120)
    phone=models.CharField(max_length=12)
    username=models.CharField(max_length=120,unique=True)
    password=models.CharField(max_length=120)

    def __str__(self):
        return self.username
