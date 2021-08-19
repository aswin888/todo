from django.shortcuts import render,redirect
from .models import Tasks
from .forms import *
# Create your views here.

def index(request):
	data = Tasks.objects.all()
	form = TasksForm()
	context={"data":data,"form":form}
	if(request.method == "POST"):
		form = TasksForm(request.POST)
		if(form.is_valid()):
			form.save()
		return redirect('/')
	return render(request,'todos/list.html',context)


def updateTask(request,pk):
	task = Tasks.objects.get(id=pk)
	form = TasksForm(instance=task)
	if(request.method == "POST"):
		form = TasksForm(request.POST,instance = task)
		if(form.is_valid()):
			form.save()
		return redirect('/')
	context = {"form":form}
	return render(request,'todos/update.html',context)