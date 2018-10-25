from django import forms
from captcha.fields import ReCaptchaField


class SelectForm(forms.Form):
	Select = forms.ChoiceField(choices=(('Username','Имя Пользователя'),('Date','Дата')))
	Select_2 = forms.ChoiceField(choices=(('Asc','Возрастание'),('Desc','Убывание')))


class AddForm(forms.Form):
	Username = forms.CharField()
	Email = forms.EmailField()
	Reference = forms.URLField()
	Image = forms.ImageField()
	Text = forms.Textarea()
	Captcha = ReCaptchaField(public_key='6LcR1XYUAAAAACh3ObqnJ2IaBRgkClvy3Sjm-s7M')
