from django.urls import re_path,path,include
from products import views 
from rest_framework import routers
from .views import ChatViewSet


router = routers.DefaultRouter()
router.register(r'chat', ChatViewSet)

urlpatterns = [ 
    path('', include(router.urls)),
]