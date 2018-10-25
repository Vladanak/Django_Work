from django import forms


class UserForm(forms.Form):
	Select = forms.ChoiceField(choices=(('Username','Имя Пользователя'),('Date','Дата')))
	Select_2 = forms.ChoiceField(choices=(('Asc','Возрастание'),('Desc','Убывание')))