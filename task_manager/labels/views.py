from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import LabelForm
from .models import Label


class LabelsListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'labels/list.html'
    context_object_name = 'labels'


class LabelCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/form.html'
    success_url = reverse_lazy('labels:list')  
    success_message = 'Метка успешно создана'


class LabelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/form.html'
    success_url = reverse_lazy('labels:list')
    success_message = 'Метка успешно изменена'


class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels:list')
    
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.object = self.get_object()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        label = self.object
        
        if label.tasks.exists():
            context['error_message'] = 'Невозможно удалить метку, ' \
                           'потому что она используется'
        
        return context
    
    def get(self, request, *args, **kwargs):
        if self.object.tasks.exists():
            return self.render_to_response(self.get_context_data())
        
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        if self.object.tasks.exists():
            messages.error(
                request, 
                'Невозможно удалить метку, потому что она используется'
            )
            return redirect('labels:list')
        
        try:
            response = super().post(request, *args, **kwargs)
            messages.success(request, 'Метка успешно удалена')
            return response
        except ProtectedError:
            messages.error(
                request, 
                'Невозможно удалить метку, потому что она используется'
            )
            return redirect('labels:list')
