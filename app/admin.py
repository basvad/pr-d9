from django.contrib import admin
from app.models import Category,Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display= ('name','slug')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display= ('title','slug' , 'status','content', 'updated', 'publication_date' , 'category')

