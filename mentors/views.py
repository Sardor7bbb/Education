from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from mentors.models import Mentor
from mentors.serializers import MentorSerializer, MentorDetailSerializer
from users.models import UserModel


class RegisterCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MentorSerializer


class MentorDetailView(generics.RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = MentorDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        if user.role != 'Mentor':
            raise PermissionDenied("You are not authorized to access this mentor profile.")
        return user

