from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from users.serializers import CreateUserSerializer, LoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from users.models import UserModel


class RegisterView(generics.CreateAPIView):
    queryset = UserModel
    serializer_class = CreateUserSerializer


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

