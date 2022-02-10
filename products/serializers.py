from rest_framework import serializers 
from products.models import Product
from users.serializers import UserSerializer
from users.models import User

class ProductSerializer(serializers.ModelSerializer):
    seller_name = serializers.SerializerMethodField()

    def get_seller_name(self, obj):
        return obj.seller.name
    class Meta:
        model = Product
        fields = ('id','name','price','seller','seller_name')
    
    # def create(self,validate_data):
    #     validate_data['seller_id']=1
    #     print(validate_data)
    #     product = Product.objects.create(**validate_data)
    #     # print(product)
    #     return product