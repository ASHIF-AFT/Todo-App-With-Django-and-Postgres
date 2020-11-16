from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .models import Todo
# Create your views here.

def list_todo(request):
    context= { 'todo_list':Todo.objects.all()}
    return render(request,'todo/list_todo.html',context)


def insert_item(request:HttpRequest):
    todo = Todo(content = request.POST['content'])
    todo.save()
    return redirect("/")

def delete_item(request,todo_id):
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect("/")


