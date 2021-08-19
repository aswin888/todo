from django.shortcuts import render,redirect
from .models import Tasks
from .forms import *
# Create your views here.

def index(request):
	data = Tasks.objects.all()
	print(data)

	form = TasksForm()
	context={"data":data,"form":form}
	if(request.method == "POST"):
		form = TasksForm(request.POST)
		if(form.is_valid()):
			form.save()
		return redirect('/todos/')
	return render(request,'todos/list.html',context)