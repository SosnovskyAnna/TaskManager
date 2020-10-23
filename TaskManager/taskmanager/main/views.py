from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth import authenticate, login


def index(request):
    tasks_N = Task.objects.filter(status='N')
    tasks_P = Task.objects.filter(status='P')
    tasks_I = Task.objects.filter(status='I')
    tasks_R = Task.objects.filter(status='R')
    tasks = [("Новые", tasks_N),
             ("Запланированные", tasks_P),
             ("В процессе", tasks_I),
             ("Завершенные", tasks_R)
             ]
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks}

                  )


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'форма не верная'

    form = TaskForm()
    context = {
        "form": form
    }
    return render(request, 'main/create.html', context)


def edit(request, id):
    task = Task.objects.get(id=id)
    print(task)
    error = ""
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'форма не верная'

    form = TaskForm(initial={
        "title": task.title,
        "task": task.task,
        "status": task.status,
        "finalTime": task.finalTime})

    context = {
        "form": form
    }

    return render(request, 'main/edit.html', context)


def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('home')

def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return redirect('error')
