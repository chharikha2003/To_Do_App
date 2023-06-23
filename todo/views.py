from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from todo.models import Tasks


# Create your views here.

def addtask(request):
    task=request.POST['task']
    
    Tasks.objects.create(task=task)
    return redirect("home")
def markasdone(request,pk):
    task=get_object_or_404(Tasks,pk=pk)
    task.is_completed=True
    task.save()
    return redirect("home")
def markasundone(request,pk):
    task=get_object_or_404(Tasks,pk=pk)
    task.is_completed=False
    task.save()
    return redirect("home")
def edittask(request,pk):
    get_task=get_object_or_404(Tasks,pk=pk)
    if request.method=='POST':
        newtask=request.POST['task']
        get_task.task=newtask
        get_task.save()
        return redirect("home")
        return 
    else:
        context={
            'get_task':get_task,
        }
        return render(request,'edittask.html',context)
def deletetask(request,pk):
    task=get_object_or_404(Tasks,pk=pk)
    task.delete()
    return redirect("home")
