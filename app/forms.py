from django import forms


class SelectForm(forms.Form):
	Select = forms.ChoiceField(choices=(('Username','Имя Пользователя'),('Date','Дата')))
	Select_2 = forms.ChoiceField(choices=(('Asc','Возрастание'),('Desc','Убывание')))


class AddForm(forms.Form):
	Username = forms.CharField(min_length=4,max_length=20,help_text='Введите Имя пользователя',label='Имя пользователя')
	Email = forms.EmailField(help_text='Введите email',min_length=7)
	Reference = forms.URLField(help_text='Вставьте ссылку, если хотите',label='Ссылка',required=False)
	Image = forms.ImageField(allow_empty_file=True, help_text='Выберите картинку',label='Картинка')
	Text = forms.Textarea()
