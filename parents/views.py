from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from parents.models import Parent
from parents.serializers import ParentSerializer, ChildrenListSerializer


class ParentCreateView(CreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ParentUpdateView(UpdateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Parent, user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class ParentChildrenListView(generics.ListAPIView):
    serializer_class = ChildrenListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Parent.objects.filter(user=user)
