from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Status
from django.db.models import ProtectedError
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _


class StatusesListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/list.html'
    context_object_name = 'statuses'

class StatusCreateView(LoginRequiredMixin, CreateView):
    model = Status
    fields = ['name']
    template_name = 'statuses/form.html'
    success_url = reverse_lazy('statuses_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _('Статус успешно создан'))
        return response

class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    fields = ['name']
    template_name = 'statuses/form.html'
    success_url = reverse_lazy('statuses_list')

    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _('Статус успешно изменен'))  
        return response

class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses_list')
    
    def post(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            result = super().post(request, *args, **kwargs)
            messages.success(request, _('Статус успешно удален'))
            return result
        except ProtectedError:
            messages.error(request, _('Невозможно удалить статус, связанный с задачами'))
            return redirect('statuses_list')

