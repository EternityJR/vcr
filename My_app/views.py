from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import Manual, User, Module, Theory, Task, Attempt


def index(request):
    return render(request, "index.html")


def manual(request, cmd_name='ADD'):
    cmd_set = Manual.objects.all().order_by("command_name")
    cmd_set_data = []
    for i in cmd_set:
        cmd_set_data.append(i.command_name)  # имена команд
    cmd = cmd_set.get(command_name=cmd_name)
    cmd = {"cmd": cmd.command_name, "description": cmd.cmd_description}
    data = {"cmd_set": cmd_set_data, "cmd": cmd}
    return render(request, "manual.html", context=data)


def task(request, task_id=1):
    task_set = Task.objects.all()
    task_set_data = []
    for i in task_set:
        task_set_data.append(i.task_name)  # имена задач
    task_obj = task_set.get(pk=task_id)
    task_obj = {"task_name": task_obj.task_name, "description": task_obj.condition, "id": task_obj.id}
    # работа с формой
    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            attempt = Attempt()
            attempt.user_id = User.objects.get(pk=1)
            attempt.task_id = Task.objects.get(pk=task_id)
            attempt.source_file = request.POST.get("source_file")
            attempt.save()
    else:
        form = CodeForm()
    data = {"task_set": task_set_data, "task_obj": task_obj, "form": form}
    return render(request, "task.html", context=data)


def theory(request, theme_id=1):
    theme_set = Theory.objects.all().order_by("pk")
    theme_set_data = []
    for i in theme_set:
        theme_set_data.append(i.theme_name)  # имена тем
    theme = theme_set.get(pk=theme_id)

    theme = {"name": theme.theme_name, "description": theme.description, "id": theme.id}
    data = {"theme_set": theme_set_data, "theme": theme}
    return render(request, "theory.html", context=data)


def auth(request):
    return render(request, "auth.html")


def reg(request):
    return render(request, "reg.html")
