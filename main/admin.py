from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Furniture, FurnitureImage
# Register your models here.


class FurnitureInline(admin.TabularInline):
    model = Furniture
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )

    inlines = [
        FurnitureInline, 
    ]


@admin.register(Furniture)
class FurnitureAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'color', 'price')


@admin.register(FurnitureImage)
class FurniturImageAdmin(admin.ModelAdmin):
    list_display = ('furniture', 'view_image')

    def view_image(self, furniture_image):
        return mark_safe(f'<img src="{furniture_image.image.url}" width="60" height="60" />')
    view_image.short_description = 'Picture'

