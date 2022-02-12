#from typing_extensions import blank
from django.db import models

from users.models import User

# Create your models here.


class Governorate(models.Model):
    name = models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.name
    
    
class Property(models.Model):
  #  name = models.CharField(max_length=70, blank=False, default='')

    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    
    governorate = models.ForeignKey(Governorate,on_delete=models.CASCADE ,blank=False)
    area = models.CharField(max_length=30,blank=False)
    street = models.CharField(max_length=30, blank=False)
    building_number = models.IntegerField(blank=False)
    propert_number = models.IntegerField(blank=False)
    
    price = models.IntegerField( default='',blank=False)
    describiton = models.TextField()
    size = models.CharField(max_length=20,blank=False)

    
    
class Comment(models.Model):
   # rate = models.IntegerField()
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
   # reports = models.IntegerField(default = 0)

    def __str__(self):
        return self.project.describiton




    