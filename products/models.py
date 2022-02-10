from django.db import models

from users.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    price = models.IntegerField(blank=False, default='')
    seller = models.ForeignKey(User, on_delete=models.CASCADE)