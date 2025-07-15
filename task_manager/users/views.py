from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CustomUserUpdateForm

User = get_user_model()

class IndexView(TemplateView):
    template_name = 'users/index.html'

class UserListView(ListView):
    model = User
    template_name = 'users/list.html'
    context_object_name = 'users'
    ordering = ['id']


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm 
    template_name = 'users/registration_form.html'
    success_url = reverse_lazy('login')
    success_message = _("Пользователь успешно зарегистрирован")


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = CustomUserUpdateForm  
    template_name = 'users/registration_form.html'
    success_url = reverse_lazy('users_list')
    success_message = _("Пользователь успешно изменен")
    login_url = reverse_lazy('login')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj != self.request.user:
            return None
        return obj

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.object:
            messages.error(request, _('У вас нет прав для изменения другого пользователя.'))
            return redirect(self.success_url)
        return super().get(request, *args, **kwargs)

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users_list')
    login_url = reverse_lazy('login')

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        if user.authored_tasks.exists() or user.assigned_tasks.exists():
            messages.error(
                request,
                _('Невозможно удалить пользователя, потому что он связан с задачей')
            )
            return redirect('users_list')
        
        response = super().post(request, *args, **kwargs)
        messages.success(request, _('Пользователь успешно удален'))
        return response

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _('Вы залогинены'))
        return response
    
    def get_success_url(self):
        return reverse_lazy('index')

class UserLogoutView(LogoutView):
    next_page = '/'
    
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.success(request, _('Вы разлогинены'))
        return response
