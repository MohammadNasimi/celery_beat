from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
#accounts
from accounts.models import User
from accounts.serializers import LoginSerializer
# jwt
from rest_framework_simplejwt.tokens import RefreshToken
#django auth 
from django.contrib.auth import authenticate
# Create your views here.
class LoginView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):
        if "password" not in request.data or "phone" not in request.data:
            return Response({"detail": "اطلاعات ارسالی کامل نیست."} , status=status.HTTP_400_BAD_REQUEST)
        def get_token(user):
                refresh = RefreshToken.for_user(user)
                return {
                    'refresh':str(refresh),
                    'access':str(refresh.access_token)
                }

        user = authenticate(phone = request.data['phone'],password = request.data['password'])
        if user :
            data = LoginSerializer(user).data
            token=get_token(user)
            data['refresh']=token['refresh']
            data['access']=token['access']


            return Response(data, status=status.HTTP_200_OK)

        else:
            return Response({'user':'wrong username or password'}, status=status.HTTP_200_OK)