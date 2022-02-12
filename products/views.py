from pydoc import describe
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from products.models import Governorate, Property
from products.serializers import PropertySerializer ,GovernorateSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.db.models import Avg, Count, Q, Sum



@api_view(['GET'])
def all_property(request):
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

@api_view(['POST', 'DELETE'])
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
    if request.method == 'POST':
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
    
    
    
    
@api_view(['GET'])
def all_governorate(request):
    governorate  = Governorate.objects.all()
    governorate_serializer = GovernorateSerializer(governorate, many=True)
    return JsonResponse(governorate_serializer.data, safe=False)


@api_view(['GET'])
def search_prop(request,searchtext):
   # query = request.GET.get('searchBox') #get the input text from template
        #filter and save the returned result into result array 
    if request.method == 'GET':   
        print(searchtext)
        result = Property.objects.filter(Q(describiton__icontains = searchtext))
        
        property_serializer = PropertySerializer(result, many=True)
        return JsonResponse(property_serializer.data, safe=False)


@api_view(['GET'])
def filterByGover(request,pk):
    if request.method == 'GET':   
        print(pk)
       

        gov_values = pk.split(",")
        print(gov_values)
        result = Property.objects.filter(governorate__id__in = gov_values)
      #  result = Property.objects.filter(id = pk)
    
        
        property_serializer = PropertySerializer(result, many=True)
        return JsonResponse(property_serializer.data, safe=False)