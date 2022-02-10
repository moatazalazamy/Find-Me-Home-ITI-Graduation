from django.urls import re_path,path,include
from products import views 
from rest_framework import routers
#from .views import ItemViewSet
router = routers.DefaultRouter()
#router.register(r'viewset', ItemViewSet)
urlpatterns = [ 
    re_path(r'^api/property$', views.property_list),
    re_path(r'^api/property/user$', views.user_property_list),
    re_path(r'^api/property/(?P<pk>[0-9]+)$', views.del_property),
    path('', include(router.urls)),
]