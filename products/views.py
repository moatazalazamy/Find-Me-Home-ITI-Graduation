from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
        #return Response(serializer.data)

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def product_list(request):
    # GET list of products, POST a new product, DELETE all products
    if request.method == 'GET':
        products = Product.objects.all()
        user = request.GET.get('user')
        if user:
            products = products.filter(seller__name=user)
        price = request.GET.get('price')
        if price:
            if price == "max":
                products = products.order_by('-price')
            elif price =='min':
                products = products.order_by('price')
        products_serializer = ProductSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)
    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        product_data['seller'] = request.user.id
        print(product_data)
        product_serializer = ProductSerializer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse(product_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE'])
@permission_classes([IsAuthenticated])
def del_product(request,pk):
    # GET list of products, POST a new product, DELETE all products
    if request.method == 'DELETE':
        product = Product.objects.get(pk=pk)
        product.delete() 
        return JsonResponse({'message': 'Product was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT': 
        product = Product.objects.get(pk=pk)
        product_data = JSONParser().parse(request) 
        product_serializer = ProductSerializer(product, data=product_data) 
        if product_serializer.is_valid(): 
            product_serializer.save() 
            return JsonResponse(product_serializer.data) 
        return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_product_list(request):
    # GET all published products
    products = Product.objects.filter(seller=request.user)
        
    if request.method == 'GET': 
        products_serializer = ProductSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)