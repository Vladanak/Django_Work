from django.contrib import admin
from .models import Book,Captcha

admin.site.register(Book)
admin.site.register(Captcha)

list_display = ['title', 'category', 'likes', 'dislikes', 'slug', 'image', 'image_img', 'timestamp', 'autor']
readonly_fields = ['image_img',]
fields = ['category', 'title', 'slug', 'metakey', 'metadesc', 'text_redactor', 'text_redactor_full', 'tag', 'timestamp', 'autor', 'image', 'image_img', 'body', 'likes', 'dislikes']