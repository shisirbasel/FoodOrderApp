from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#additional user details model to store phonenumber
class UserDetails(models.Model):
    
    phone = models.BigIntegerField(max_length=10, verbose_name="Phone Number", primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User")
    
    def __str__(self):
        return self.user
    
class Food(models.Model):

    foodname = models.CharField(max_length=200,verbose_name="Food Item")
    price = models.FloatField()
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return f"{self.foodname}"
    
class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    


    
