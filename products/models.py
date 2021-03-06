#from typing_extensions import blank
from django.db import models

from users.models import User
import uuid
import os
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


class Comments(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=255, default="")
    propty = models.ForeignKey(Property, on_delete=models.CASCADE)



# function to generate unique name for uploaded imgs
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('properties/', filename)


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    img = models.ImageField(upload_to=get_file_path)

    def __str__(self):
        return self.project.title

    