from ntpath import realpath
from django.db import models
from users.models import User

# Create your models here.
class Chat(models.Model):
    messege = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    sender =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users1')