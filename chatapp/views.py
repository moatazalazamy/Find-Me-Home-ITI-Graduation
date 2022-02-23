from django.dispatch import receiver
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import ChatSerializer , RoomSerializer
from rest_framework.response import Response
from users.models import User
from .models import Chat ,Room
from django.http.response import JsonResponse
from rest_framework.permissions import IsAuthenticated
from itertools import chain
from django.db.models import Q
from rest_framework.decorators import api_view


# Create your views here.
class ChatViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    def create(self, request):
        sender = request.user
        reciever = User.objects.filter(id=request.data['id']).first()     
        request.data['sender'] = sender.id
        request.data['reciever'] = reciever.id
        serializer = ChatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def list(self, request):
        sender = request.user
        messages = Chat.objects.filter(Q(sender=sender.id) | Q(reciever=sender.id))
        print(messages)
        result = []
        for message in messages:
            if message.sender_id not in result and message.sender_id != sender.id :
                result.append(message.sender_id)
            if message.reciever_id not in result and message.reciever_id != sender.id:
                result.append(message.reciever_id)    
        return JsonResponse(result, safe=False) 

    def retrieve(self, request, pk, *args, **kwargs):
        sender = request.user
        reciever = User.objects.filter(id=pk).first() 
        sender_messages = Chat.objects.filter(sender=sender.id, reciever=reciever.id)
        reciever_messages = Chat.objects.filter(sender=reciever.id, reciever=sender.id)
        messages = list(chain(sender_messages, reciever_messages))
        messages  =  sorted(messages, key=lambda msg: msg.created_at)
        serializer = ChatSerializer(messages, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    
    
    
@api_view(['GET'])
def all_rooms(request):
    rooms  = Room.objects.all()
    rooms_serializer = RoomSerializer(rooms, many=True)
    return JsonResponse(rooms_serializer.data, safe=False)
