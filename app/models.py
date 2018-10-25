from django.db import models


class Book(models.Model):
	Username = models.CharField(max_length=30,blank=False,unique=True)
	Email = models.EmailField(unique=True,blank=False)
	Reference = models.URLField(null=True,blank=True)
	Text = models.TextField(max_length=300,blank=False)
	CAPTCHA = models.TextField(blank=False)
	Image = models.ImageField(upload_to='images/',blank=True,null=True)
	Date = models.DateTimeField(blank=False)
	User_Ip = models.GenericIPAddressField(blank=False)
	Browser_Info = models.TextField(blank=False)