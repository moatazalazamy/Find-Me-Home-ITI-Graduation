from rest_framework import serializers 
from users.serializers import UserSerializer
from users.models import User
from chatapp.models import Chat

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id','messege','created_at','sender','reciever') 
    order_by = (('created_at',))