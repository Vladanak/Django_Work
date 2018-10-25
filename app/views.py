import requests
from django.shortcuts import  render_to_response
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import messages
from .models import Captcha
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from .forms import SelectForm
from .forms import AddForm


def message(request):
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
				form.save()
				messages.success(request, 'New comment added with success!')
			else:
				messages.error(request, 'Invalid reCAPTCHA. Please try again.')
			return redirect('/')

	add_form = AddForm()
	return render(request,'Messages.html',{'form':add_form})


@csrf_exempt
def index(request):
	user_form = SelectForm()
	if(request.method == 'POST'):
		value = request.POST
		if (value['Select'] == 'Username'):
			if (value['Select_2'] == 'Asc'):
				return render_to_response("index.html",{'books':Book.objects.order_by('Username')[0:9],"form": user_form})
			else:
				return render_to_response("index.html", {'books': Book.objects.order_by('Username').reverse()[0:9],"form": user_form})
		else:
			if (value['Select_2'] == 'Asc'):
				return render_to_response("index.html", {'books': Book.objects.order_by('Date')[0:9],"form": user_form})
			else:
				return render_to_response("index.html", {'books': Book.objects.order_by('Date').reverse()[0:9],"form": user_form})
	else:
		return render(request, "index.html", {"form": user_form, "books": Book.objects.order_by('id').reverse()[0:9]})
