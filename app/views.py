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
	add_form = AddForm()
	return render(request,'Messages.html',{'form':add_form})


def index(request):
	schedule.run_pending()
	obj_list = Book.objects.all()
	obj_list = obj_list.order_by('id').reverse()
	paginator = Paginator(obj_list,10)
	page = request.GET.get('page')
	contacts = paginator.get_page(page)
	user_form = SelectForm()
	if request.method == 'POST':
		value = request.POST
		if value['Select'] == 'Username':
			if value['Select_2'] == 'Asc':
				obj_list = obj_list.order_by('Username')
				paginator = Paginator(obj_list, 10)
				page = request.GET.get('page')
				contacts = paginator.get_page(page)
				return render(request,"index.html", {"form": user_form,"count":obj_list,'contacts':contacts})
			else:
				obj_list = obj_list.order_by('Username').reverse()
				paginator = Paginator(obj_list, 10)
				page = request.GET.get('page')
				contacts = paginator.get_page(page)
				return render(request,"index.html", {"form": user_form,"count":obj_list,'contacts':contacts})
		else:
			if value['Select_2'] == 'Asc':
				obj_list = obj_list.order_by('Date')
				paginator = Paginator(obj_list, 10)
				page = request.GET.get('page')
				contacts = paginator.get_page(page)
				return render(request,"index.html", {"form": user_form,"count":obj_list,'contacts':contacts})
			else:
				obj_list = obj_list.order_by('Date').reverse()
				paginator = Paginator(obj_list, 10)
				page = request.GET.get('page')
				contacts = paginator.get_page(page)
				return render(request,"index.html", {"form": user_form,"count":obj_list,'contacts':contacts})
	else:
		return render(request, "index.html", {"form": user_form,"count":obj_list,'contacts':contacts})