from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser

from courses.models import CourseModel
from courses.serializers import CourseSerializer, CourseListSerializer


class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUser]


class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUser]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = CourseModel.objects.all()
    serializer_class = CourseListSerializer
    permission_classes = [IsAdminUser]
