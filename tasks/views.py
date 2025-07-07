from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.shortcuts import redirect

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/list.html'
    context_object_name = 'tasks'

class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/form.html'
    success_url = reverse_lazy('tasks_list')
    success_message = _('Задача успешно создана')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/form.html'
    success_url = reverse_lazy('tasks_list')
    success_message = _('Задача успешно изменена')

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks_list')
    success_message = _('Задача успешно удалена')

    def test_func(self):
        task = self.get_object()
        return task.author == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, _('Задачу может удалить только ее автор'))
        return redirect('tasks_list')

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/detail.html'
