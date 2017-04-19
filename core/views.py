from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Task
from django.http import HttpResponseRedirect
from django.urls import reverse
from .helpers import populate


def task_populate(request):
    populate()
    return HttpResponseRedirect(reverse('core:task-list'))


def task_delete_all(request):
    Task.objects.all().delete()
    return HttpResponseRedirect(reverse('core:task-list'))


class TaskList(ListView):
    model = Task


class TaskDetail(DetailView):
    model = Task


class TaskCreate(CreateView):
    model = Task
    fields = ['title']
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('core:task-list')


class TaskUpdate(UpdateView):
    model = Task
    fields = ['title']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('core:task-list')


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('core:task-list')
