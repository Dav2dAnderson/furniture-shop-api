from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import Category, Furniture, FurnitureImage
from .serializers import CategorySerializer, FurnitureSerializer, FurnitureImagesSerializer
# Create your views here.


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        else:
            return request.user and request.user.is_staff  


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly, ]


class FurnitureViewSet(viewsets.ModelViewSet):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer
    permission_classes = [IsAdminOrReadOnly, ]


class FurnitureImageViewSet(viewsets.ModelViewSet):
    queryset = FurnitureImage.objects.all()
    serializer_class = FurnitureImagesSerializer
    permission_classes = [IsAdminOrReadOnly, ]
