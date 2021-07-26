from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages

from .models import Task
from .forms import TaskForm

# Create your views here.


@login_required()
def tasks(request):
    context = {}
    tasks = Task.objects.all()
    context['parent'] = 'Tasks'
    context['page'] = 'Schedule'
    context['tasks'] = tasks
    return render(request, 'tasks/tasks.html', context)


@login_required()
def edit_task(request, id=None, context=None):
    context = context or {}
    if id:
        task = Task.objects.get(pk=id)
        task_form = TaskForm(request.POST or None, instance=task)
    else:
        task_form = TaskForm(request.POST or None)

    if task_form.is_valid():
        if not id:
            user = task_form.save(commit=False)
            user.created_by_id = request.user.id
            user.name_id = request.user.id
            user.save()
            messages.success(request, 'Time added')
            return redirect('tasks:tasks')

        else:
            task = task_form.save(commit=False)
            task.save()
            messages.success(request, 'Time  updated')
            return redirect('tasks:tasks')

    context['form'] = task_form
    context['id'] = id
    context['parent'] = 'Tasks'
    context['add_page'] = 'Add Time'
    context['edit_page'] = 'Edit Time'
    return render(request, 'tasks/edit_task.html', context)


@login_required()
def task_delete(request, id):
    context = {}

    task = Task.objects.get(pk=id)
    Task.objects.filter(id=task.id).update(deleted=True)
    messages.success(request, 'Time  deleted')
    return redirect('tasks:tasks')
