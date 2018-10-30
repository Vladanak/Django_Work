from django.contrib import admin
from .models import Book
from .models import Captcha


class ImageAdmin(admin.ModelAdmin):
	list_display = ['Username', 'Email', 'Reference', 'Text', 'image_img', 'Date',
					'User_Ip', 'Browser_Info']
	readonly_fields = ['image_img', ]


admin.site.register(Captcha)
admin.site.register(Book, ImageAdmin)
