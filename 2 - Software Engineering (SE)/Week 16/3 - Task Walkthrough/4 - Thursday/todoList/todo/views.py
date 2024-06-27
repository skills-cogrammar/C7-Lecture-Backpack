from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

def create(request):
    if request.method == 'POST':
        form =TodoForm(request.POST)

        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todos')
        
    else:
        form = TodoForm()

    return render(request, 'todo_form.html', {'form': form})

def get_all(request):
    todos = Todo.objects.all()

    context = {
        'todos': todos,
        'page_title': 'Show all To-dos'
    }

    return render(request, 'all_todos.html', context=context)

def get(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    context = {
        'todo': todo
    }

    return render(request, 'todo.html', context=context)

def update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)

        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todos')
        
    else:
        form = TodoForm()

    return render(request, 'todos_form.html', {'form': form})
        
def delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todos')