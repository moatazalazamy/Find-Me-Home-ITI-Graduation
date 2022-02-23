from django.urls import re_path,path,include
from products import views 
from rest_framework import routers
from .views import ChatViewSet ,all_rooms

router = routers.DefaultRouter()
router.register(r'chat', ChatViewSet)

urlpatterns = [ 
    re_path(r'^allrooms$',all_rooms),
    path('', include(router.urls)),
]