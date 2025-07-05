from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class UserListView(ListView):
    model = User
    template_name = 'users/list.html'
    context_object_name = 'users'

class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'users/form.html'
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
    template_name = 'users/form.html'
    fields = ['first_name', 'last_name', 'username']
    success_url = reverse_lazy('users_list')
    success_message = "Пользователь успешно изменён"
    login_url = reverse_lazy('login')

    def get_object(self, queryset=None):
        return self.request.user  # Только текущий пользователь

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users_list')
    login_url = reverse_lazy('login')

    def get_object(self, queryset=None):
        return self.request.user  # Только текущий пользователь

class UserLoginView(LoginView):
    template_name = 'users/login.html'

class UserLogoutView(LogoutView):
    next_page = '/'
def index(request):
    return HttpResponse("Welcome to Hexlet Code!")

class IndexView(TemplateView):
    template_name = 'home/index.html'


