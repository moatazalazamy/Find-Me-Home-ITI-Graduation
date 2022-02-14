from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
import jwt, datetime
from django.conf import settings

from django.http.response import JsonResponse


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        response = Response()
        
        user = User.objects.filter(id=payload['user_id']).first()
        serializer = UserSerializer(user)


       # response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token,
            'user': serializer.data

        }
        return response


class UserView(APIView):

    def get(self, request):
       # token = request.COOKIES.get('jwt')
        token = request.headers.get('jwt')

        

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:    
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        except:
            raise AuthenticationFailed('Unauthenticated!')
        user = User.objects.filter(id=payload['user_id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
    
    
class Allusers(APIView):
    def get(self,request):
        user = User.objects.all()
        users = UserSerializer(user, many=True)
        #response.set_cookie(key='jwt', value=token, httponly=True)
        usrdata = users.data
        usrnames = []
        #print(usrdata)
        for i in range(len(user)):
            a = list(usrdata[i].values())
            usrnames.append(a[1])
            print(usrnames)
        return JsonResponse(usrnames, safe=False)
