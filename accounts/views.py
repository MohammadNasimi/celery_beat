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
        
        
############register  ##################
class RegisterView(generics.APIView):
    def post(self, request, *args, **kwargs):
        email= request.data.get("email" ,"")
        first_name= request.data.get("first_name" ,"")
        last_name= request.data.get("last_name" ,"")
        # create-user
        def create_user():
            user =User.objects.create_user(phone=request.data.get('phone'),password=request.data.get('password'),
                email=email,first_name=first_name,
                last_name=last_name)
            return user
        
        
        if request.data.get('phone') == None or request.data.get('password') == None \
                            or request.data.get('password2') == None:
                return Response({"detail": "اطلاعات ارسالی کامل نیست."} , status=status.HTTP_400_BAD_REQUEST)
        try:
            if request.data.get('password')==request.data.get('password2'):
                user =create_user()
            else:
                return Response({'detail:':'password must to mutch'},
                                status=status.HTTP_400_BAD_REQUEST)
        except:
                return Response({"detail"  : "username exist"} , status=status.HTTP_400_BAD_REQUEST)
        return Response(request.data, status=status.HTTP_201_CREATED)