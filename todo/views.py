from django.shortcuts import render
from .models import ToDoItem

# Create your views here.

def todo_list(request):
    todos=ToDoItem.objects.all()
    return render(request,'todo/todo_list.html',{'todos':todos})

