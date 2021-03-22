from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Todo
from .forms import TodoForm


def signup(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    return render(request, 'my_todo/signup.html', {"form": form})



@login_required
def createtodo(request):
    todo = Todo.objects.all().order_by('-date_created')
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = TodoForm()
    return render(request, 'my_todo/create.html',{"form":form, "todo":todo})

         
def updatetodo(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("/")

    return render(request, 'my_todo/update.html', {"todo":todo, "form":form})

def deletetodo(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect("/")
