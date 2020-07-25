from app.models import Post,Category 
from rest_framework import serializers
from django.contrib.auth.models import User  

#здесь описаны все сериализаторы, используемые в приложении
class AuthorSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = User  
        fields = ['username', 'first_name', 'last_name']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)  
    class Meta:  
        model = Post  
        fields = '__all__'

#сериализатор постов
class CategorySerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Category  
        fields = '__all__'

