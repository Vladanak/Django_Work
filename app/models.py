from django.db import models


class Book(models.Model):
	Username = models.CharField(max_length=30,blank=False,unique=True)
	Email = models.EmailField(unique=True,blank=False)
	Reference = models.URLField(null=True,blank=True)
	Text = models.TextField(max_length=300,blank=False)
	Image = models.ImageField(upload_to='images/media/',blank=True,null=True)
	Date = models.DateTimeField(blank=False)
	User_Ip = models.GenericIPAddressField(blank=False)
	Browser_Info = models.TextField(blank=False)

	def image_img(self):
		if self.Image:
			from django.utils.safestring import mark_safe
			return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.Image.url))
		else:
			return '(Нет изображения)'

	image_img.short_description = 'Картинка'
	image_img.allow_tags = True


class Captcha(models.Model):
	CAPTCHA = models.TextField(blank=True, default='6LcR1XYUAAAAAKgKVOvGrpPUvqka_4kP7ZkjEgj9')