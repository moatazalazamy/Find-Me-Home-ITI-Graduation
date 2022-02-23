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
    re_path(r'^api/allproperty$', views.all_property),
    re_path(r'^api/allgovernorate$', views.all_governorate),
    re_path(r'^api/search/(?P<searchtext>.+)$', views.search_prop),
    re_path(r'^api/filter/(?P<pk>.+)$', views.filterByGover),
    re_path(r'^api/addimages$', views.PostView.as_view()),
    re_path(r'^api/getimages/(?P<pk>.+)$', views.add_image),

    re_path(r'^api/propinfo/(?P<pk>.+)$', views.get_property),

    
    path('', include(router.urls)),
]