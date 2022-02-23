from pyexpat import model
from statistics import mode
from rest_framework import serializers 
from users.serializers import UserSerializer
from users.models import User
from chatapp.models import Chat ,RoomMessage ,Room

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id','messege','created_at','sender','reciever') 
    order_by = (('created_at',))
    
    
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room 
        fields = '__all__'
