from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, FurnitureViewSet, FurnitureImageViewSet


router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('furniture', FurnitureViewSet)
router.register('furniture_images', FurnitureImageViewSet)

urlpatterns = [
    path('', include(router.urls))
]