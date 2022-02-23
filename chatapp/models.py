from ntpath import realpath
from django.db import models
from users.models import User

# Create your models here.
class Chat(models.Model):
    messege = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    sender =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users1')
	
	
	
	
class Room(models.Model):
    name = models.CharField(max_length=255)

    
    
class RoomMessage(models.Model):
    room = models.ForeignKey(Room,related_name='messages',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='messages',on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ('date_added',)