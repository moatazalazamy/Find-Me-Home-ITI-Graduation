from django.urls import path, re_path
from .views import RegisterView, LoginView, UserView, LogoutView,Allusers,UpdateUser

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('allusers', Allusers.as_view()),
    re_path(r'^update/(?P<pk>[0-9]+)$', UpdateUser.as_view())

]
