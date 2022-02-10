from rest_framework import serializers
from products.models import Governorate 
from products.models import Property
from users.serializers import UserSerializer
from users.models import User

class PropertySerializer(serializers.ModelSerializer):
   # seller = serializers.SerializerMethodField()
  #  governorate_id = serializers.RelatedField(source='governorate',read_only=True)
   # seller_id = serializers.RelatedField(source='seller',read_only=True)
    seller = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)
    governorate = serializers.PrimaryKeyRelatedField(queryset=Governorate.objects.all(),many=False)
 
    def get_seller(self, obj):
        return obj.seller.name
    
    def get_governorate(self, obj):
        return obj.governorate.name
    
    class Meta:
        model = Property
        fields = ('id','describiton','price','seller','size','governorate' , 'area','street','building_number','propert_number')

	