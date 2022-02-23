from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
import os

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('profilepics/', filename)

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    profileimg = models.ImageField(upload_to=get_file_path, default=None)
    phonenum = models.CharField(max_length=11, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f"{self.name}"
