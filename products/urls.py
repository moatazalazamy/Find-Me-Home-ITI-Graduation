from django.urls import re_path,path,include
from products import views 
from rest_framework import routers
from .views import ItemViewSet
router = routers.DefaultRouter()
router.register(r'viewset', ItemViewSet)
urlpatterns = [ 
    re_path(r'^api/products$', views.product_list),
    re_path(r'^api/products/user$', views.user_product_list),
    re_path(r'^api/products/(?P<pk>[0-9]+)$', views.del_product),
    path('', include(router.urls)),
]