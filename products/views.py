from pydoc import describe
from unittest import result
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from products.models import Governorate, Property ,PropertyImage, Comments
from products.serializers import PropertySerializer ,GovernorateSerializer,PropertyADDSerializer,PropertyImgSerializer,CommentsSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.db.models import Avg, Count, Q, Sum
from django.core.files.storage import default_storage

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status




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
        properties_serializer = PropertyADDSerializer(properties, many=True)
        
        return JsonResponse(properties_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    if request.method == 'POST':
        property_data = JSONParser().parse(request)
        property_data['seller'] = request.user.id
        property_serializer = PropertyADDSerializer(data=property_data)
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
        property_serializer = PropertyADDSerializer(property, data=property_data, partial=True) 
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
    
    
@api_view(['POST','GET'])
def add_image(request):
    if request.method == 'POST':
        # file=request.FILES['file']
        propert_images = JSONParser().parse(request)
        propertyImg_serializer = PropertyImgSerializer(data=propert_images)
        print(propert_images)
        print("==============================")
        print(propert_images['image'])

        # with open(propert_images['image'], encoding="utf8", errors='ignore') as f:
            
            
            
        if propertyImg_serializer.is_valid():
                propertyImg_serializer.save()
                return JsonResponse(propertyImg_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(propertyImg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # else:
    #     result = PropertyImage.objects.filter(property__id__in = pk)
    #     propertyImg_serializer = PropertyImgSerializer(result,many=True)
    #     return JsonResponse(propertyImg_serializer.data, safe=False)

            
        
    
class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        images = PropertyImage.objects.all()
        serializer = PropertyImgSerializer(images, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        propertyImg_serializer = PropertyImgSerializer(data=request.data)
        if propertyImg_serializer.is_valid():
            propertyImg_serializer.save()
            return Response(propertyImg_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', propertyImg_serializer.errors)
            return Response(propertyImg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def comment_list(request):
    if request.method == 'GET':
        prop = request.GET.get("prop")
        if prop:
            comments = Comments.objects.filter(propty=prop)
            comments_serializer = CommentsSerializer(comments, many=True)
            return JsonResponse(comments_serializer.data, safe=False)
    elif request.method == 'POST':
        comment_data = JSONParser().parse(request)
        comment_data['commenter'] = request.user.id
        print(comment_data)
        comment_serializer = CommentsSerializer(data=comment_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse(comment_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
