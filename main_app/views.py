from dataclasses import fields
from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
from .models import Todo
from .forms import TodoForm
# Create your views here.

def home(request):
    todos = Todo.objects.all()
    totalquantity = sum(todo.quantity for todo in todos)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            new_todo = form.save(commit=False)
            new_todo.save()
            return redirect('home')
    else:
        form = TodoForm()
    return render(request, 'home.html', {'todos': todos, 'form': form, 'total': totalquantity})

class DeleteTodo(DeleteView):
    model = Todo
    success_url='/'
