from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class UserListView(ListView):
    model = User
    template_name = 'home/list.html'
    context_object_name = 'users'

class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'home/form.html'
    fields = ['username', 'first_name', 'last_name', 'password']
    success_url = reverse_lazy('login')
    success_message = "Пользователь успешно зарегистрирован"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)

class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'home/form.html'
    fields = ['first_name', 'last_name', 'username']
    success_url = reverse_lazy('users_list')
    success_message = "Пользователь успешно изменён"
    login_url = reverse_lazy('login')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj != self.request.user:
            from django.http import HttpResponseForbidden
            return HttpResponseForbidden("У вас нет прав для редактирования этого пользователя")
        return obj

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'home/delete.html'
    success_url = reverse_lazy('users_list')
    login_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        if user.authored_tasks.exists() or user.assigned_tasks.exists():
            messages.error(request, 'Невозможно удалить пользователя, связанного с задачами')
            return redirect('users_list')
        return super().post(request, *args, **kwargs)

class UserLoginView(LoginView):
    template_name = 'home/login.html'

class UserLogoutView(LogoutView):
    next_page = '/'

class IndexView(TemplateView):
    template_name = 'home/index.html'
