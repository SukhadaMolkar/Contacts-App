from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from contactsApi.settings import JWT_SECRET_KEY
from django.contrib import auth
# from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt import tokens
#from .models import User
#from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

import jwt


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer
    print("sclass",serializer_class)

    def post(self, request):
        print("here")
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    def post(self,request):
        data=request.data
        username = data.get("username","")
        password = data.get("password", "")
        print("username",username,"----password",password)
        user = auth.authenticate(username=username,password=password)
        print("----user",user)

        if user:
            auth_token = jwt.encode({"username": user.username}, JWT_SECRET_KEY)
            print("auth_token",auth_token)
            serializer = UserSerializer(user)

            data ={"user":serializer.data,"token": auth_token}
            print(data)
            return Response(data,status=status.HTTP_200_OK)

            #SEND RES
        return Response({"detail":"Invalid Credentials"},status=status.HTTP_401_UNAUTHORIZED)

