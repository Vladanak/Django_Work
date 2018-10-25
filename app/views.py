from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from .forms import UserForm


def messages(request):
	return render(request,'Messages.html',{})

@csrf_exempt
def index(request):
	user_form = UserForm()
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

