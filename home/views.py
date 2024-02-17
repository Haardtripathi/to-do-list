from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def home(request):
    if request.method=="POST":
        task=request.POST.get('task')
        new_task=Tasks(task=task)
        new_task.save()
    tasks=Tasks.objects.all()

    context={'tasks':tasks}

    return render(request,'todo.html',context)

def DeleteTask(request,id):
    delete_task=Tasks.objects.filter(id=id).delete()
    return redirect('home')

def Update(request,id):
    update_task=Tasks.objects.get(id=id)
    update_task.status=True
    update_task.save()
    return redirect('home')

    
