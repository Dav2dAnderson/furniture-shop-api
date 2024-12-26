from django.db import models
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug or self.title_has_changed():
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def title_has_changed(self):
        if not self.pk:
            return True
        old_title = Category.objects.filter(id=self.id).values_list('title', flat=True).first()
        return old_title != self.title


class Furniture(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    color = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug or self.title_has_changed():
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def title_has_changed(self):
        if not self.pk:
            return True
        old_title = Furniture.objects.filter(id=self.id).values_list('title', flat=True).first()
        return old_title != self.title


class FurnitureImage(models.Model):
    image = models.ImageField(upload_to='furniture_images/')
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE)

    def __str__(self):
        return self.furniture.title




