from django import forms


class SelectForm(forms.Form):
	Select = forms.ChoiceField(choices=(('Username','Имя Пользователя'),('Date','Дата')),label='')
	Select_2 = forms.ChoiceField(choices=(('Asc','Возрастание'),('Desc','Убывание')),label='')


class AddForm(forms.Form):
	Username = forms.CharField(min_length=4,max_length=20,label='Имя пользователя')
	Email = forms.EmailField(min_length=7)
	Reference = forms.URLField(label='Ссылка',required=False)
	Image = forms.ImageField(allow_empty_file=True,label='Картинка',required=False)
	Text = forms.CharField(max_length=3000,label='Сообщение',widget=forms.Textarea)
