from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  

class Category(models.Model):
    slug = models.CharField(max_length=128, default="")
    name = models.CharField(max_length=256)
    def __str__(self):
        return f'{self.name} ({self.slug})'

class Post(models.Model):  
    title = models.CharField(max_length=255)  
    slug = models.SlugField  
    status = models.CharField(max_length=10, choices=[('D', 'draft'), ('P', 'published')])  
    content = models.TextField()
    updated = models.DateTimeField(default=timezone.now)  
    publication_date = models.DateTimeField(default=timezone.now)
    #category = models.ManyToManyField(Category, blank=True)
    category= models.ForeignKey(Category, on_delete=models.CASCADE,default='')
    author = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)


