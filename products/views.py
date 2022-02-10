from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from products.models import Property
from products.serializers import PropertySerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def property_list(request):
    # GET list of propertys, POST a new property, DELETE all propertys
    if request.method == 'GET':
        properties = Property.objects.all()
        user = request.GET.get('user')
        if user:
            properties = properties.filter(seller__name=user)

        # price = request.GET.get('price')
        # if price:
        #     if price == "max":
        #         properties = properties.order_by('-price')
        #     elif price =='min':
        #         properties = properties.order_by('price')
        properties_serializer = PropertySerializer(properties, many=True)
        
        return JsonResponse(properties_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        property_data = JSONParser().parse(request)
        property_data['seller'] = request.user.id
        property_serializer = PropertySerializer(data=property_data)
        if property_serializer.is_valid():
            property_serializer.save()
            return JsonResponse(property_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(property_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



@api_view(['PUT','DELETE','PATCH'])
@permission_classes([IsAuthenticated])
def del_property(request,pk):
    # GET list of propertys, POST a new property, DELETE all propertys
    if request.method == 'DELETE':
        property = Property.objects.get(id=pk)
        property.delete() 
        return JsonResponse({'message': 'property was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PATCH': 
        property = Property.objects.get(id=pk)
        property_data = JSONParser().parse(request) 
        property_serializer = PropertySerializer(property, data=property_data, partial=True) 
        if property_serializer.is_valid(): 
            property_serializer.save() 
            return JsonResponse(property_serializer.data) 
        return JsonResponse(property_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_property_list(request):
    # GET all published propertys
    property = Property.objects.filter(seller=request.user)
        
    if request.method == 'GET': 
        propertys_serializer = PropertySerializer(property, many=True)
        return JsonResponse(propertys_serializer.data, safe=False)
    
    
    