import requests
import datetime
import schedule
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import messages
from .models import Captcha
from .models import Book
from .forms import SelectForm
from .forms import AddForm
from django.core.paginator import Paginator


def index_func(request,element,sort):
	paginator = Paginator(start_list(element,sort), 10)
	page = request.GET.get('page')
	contacts = paginator.get_page(page)
	return contacts


def start_list(element,sort):
	obj_list = Book.objects.all()
	if sort == 'Desc':
		obj_list = obj_list.order_by(element).reverse()
	else:
		obj_list = obj_list.order_by(element)
	return obj_list


def job():
	from django.core import management
	management.call_command('dbbackup')


schedule.every().day.at('00:00').do(job)


def message(request):
	schedule.run_pending()
	if request.method == 'POST':
		form = AddForm(request.POST)
		if form.is_valid():
			captcha = Captcha.objects.first()
			recaptcha_response = request.POST.get('g-recaptcha-response')
			data = {
				'secret': captcha.CAPTCHA,
				'response': recaptcha_response
			}
			r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
			result = r.json()
			if result['success']:
				Book.objects.create(Username=request.POST['Username'],Email=request.POST['Email'],
									Reference=request.POST['Reference'],Image=request.POST['Image'],
									Text=request.POST['Text'],User_Ip=request.META['REMOTE_ADDR'],
									Date=datetime.datetime.now(),Browser_Info=request.META['HTTP_USER_AGENT'])
				messages.success(request, 'New comment added with success!')
			else:
				messages.error(request, 'Invalid reCAPTCHA. Please try again.')
			return redirect(to='/')
	return render(request,'Messages.html',{'form': AddForm()})


def index(request):
	schedule.run_pending()
	if request.method == 'POST':
		value = request.POST
		if value['Select'] == 'Username':
			if value['Select_2'] == 'Asc':
				contacts = index_func(request,'Username','Asc')
			else:
				contacts = index_func(request,'Username','Desc')
			return render(request, "index.html", {"form": SelectForm(), "count": start_list('id','Desc'),
												  'contacts': contacts})
		else:
			if value['Select_2'] == 'Asc':
				contacts = index_func(request,'Date','Asc')
			else:
				contacts = index_func(request,'Date','Desc')
			return render(request, "index.html", {"form": SelectForm(), "count": start_list('id','Desc'),
												  'contacts': contacts})
	else:
		return render(request, "index.html", {"form": SelectForm(),"count": start_list('id','Desc'),
											  'contacts': index_func(request,'id','Desc')})