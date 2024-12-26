from rest_framework import serializers
from .models import Category, FurnitureImage, Furniture


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class FurnitureImagesSerializer(serializers.ModelSerializer):

    furniture = serializers.PrimaryKeyRelatedField(queryset=Furniture.objects.all())

    class Meta:
        model = FurnitureImage
        fields = '__all__'
        depth = 1

    
class FurnitureSerializer(serializers.ModelSerializer):

    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Furniture
        fields = '__all__'
        depth = 1

