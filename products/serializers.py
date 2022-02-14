from dataclasses import field, fields
from xml.parsers.expat import model
from rest_framework import serializers
from products.models import Governorate 
from products.models import Property ,PropertyImage
from users.serializers import UserSerializer
from users.models import User


# class Base64ImageField(serializers.ImageField):
#     """
#     A Django REST framework field for handling image-uploads through raw post data.
#     It uses base64 for encoding and decoding the contents of the file.

#     Heavily based on
#     https://github.com/tomchristie/django-rest-framework/pull/1268

#     Updated for Django REST framework 3.
#     """

#     def to_internal_value(self, data):
#         from django.core.files.base import ContentFile
#         import base64
#         import six
#         import uuid

#         # Check if this is a base64 string
#         if isinstance(data, six.string_types):
#             # Check if the base64 string is in the "data:" format
#             if 'data:' in data and ';base64,' in data:
#                 # Break out the header from the base64 content
#                 header, data = data.split(';base64,')

#             # Try to decode the file. Return validation error if it fails.
#             try:
                
#                 decoded_file = base64.b64decode(data)
#             except TypeError:
#                 self.fail('invalid_image')

#             # Generate file name:
#             file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
#             # Get the file name extension:
#             file_extension = self.get_file_extension(file_name, decoded_file)

#             complete_file_name = "%s.%s" % (file_name, file_extension, )

#             data = ContentFile(decoded_file, name=complete_file_name)

#         return super(Base64ImageField, self).to_internal_value(data)

#     def get_file_extension(self, file_name, decoded_file):
#         import imghdr

#         extension = imghdr.what(file_name, decoded_file)
#         extension = "jpg" if extension == "jpeg" else extension

#         return extension

class PropertyImgSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    # property = serializers.Field(source='property_id')
    property = serializers.PrimaryKeyRelatedField(queryset=Property.objects.all(),many=False)

    class Meta:
        model = PropertyImage
        fields = ('id','image','property')
         

class PropertySerializer(serializers.ModelSerializer):
    seller = serializers.SerializerMethodField()
  #  governorate_id = serializers.RelatedField(source='governorate',read_only=True)
   # seller_id = serializers.RelatedField(source='seller',read_only=True)
   # seller = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)
   # governorate = serializers.PrimaryKeyRelatedField(queryset=Governorate.objects.all(),many=False)
    governorate = serializers.SerializerMethodField()
    

    def get_seller(self, obj):
        return obj.seller.name
    
    def get_governorate(self, obj):
        return obj.governorate.name
    
    class Meta:
        model = Property
       # fields = ('id','describiton','price','seller','size','governorate' , 'area','street','building_number','propert_number')
        fields = '__all__'
        
class PropertyADDSerializer(serializers.ModelSerializer):
   # seller = serializers.SerializerMethodField()
  #  governorate_id = serializers.RelatedField(source='governorate',read_only=True)
   # seller_id = serializers.RelatedField(source='seller',read_only=True)
    seller = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)
    governorate = serializers.PrimaryKeyRelatedField(queryset=Governorate.objects.all(),many=False)
    #governorate = serializers.SerializerMethodField()
 

    def get_seller(self, obj):
        return obj.seller.name
    
    def get_governorate(self, obj):
        return obj.governorate.name
    
    class Meta:
        model = Property
       # fields = ('id','describiton','price','seller','size','governorate' , 'area','street','building_number','propert_number')
        fields = '__all__'
	
 
class GovernorateSerializer(serializers.ModelSerializer):
     
    class Meta:
        model= Governorate
        fields = '__all__'
        
        
