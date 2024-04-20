from django.shortcuts import render,redirect
from .models import ToDoItem
from .forms import ToDoItemForm


# Create your views here.

def todo_list(request):
    todos = ToDoItem.objects.all()
    form = ToDoItemForm()
    if request.method == 'POST':
        form = ToDoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    return render(request, 'todo/todo_list.html', {'todos': todos, 'form': form})

def complete_todo(request, todo_id):
    todo = ToDoItem.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')    
