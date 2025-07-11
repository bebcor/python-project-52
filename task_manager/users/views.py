from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _

class IndexView(TemplateView):
    template_name = 'users/index.html'

class UserListView(ListView):
    model = User
    template_name = 'users/list.html'
    context_object_name = 'users'
    ordering = ['id']

class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'users/registration_form.html'
    fields = ['username', 'first_name', 'last_name', 'password']
    success_url = reverse_lazy('login')
    success_message = _("User registered successfully")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)

class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'users/registration_form.html'
    fields = ['first_name', 'last_name', 'username']
    success_url = reverse_lazy('users_list')
    success_message = _("User updated successfully")
    login_url = reverse_lazy('login')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj != self.request.user:
            return None
        return obj

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.object:
            messages.error(request, _('You cannot edit another user'))
            return redirect(self.success_url)
        return super().get(request, *args, **kwargs)

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users_list')
    login_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        if user.authored_tasks.exists() or user.assigned_tasks.exists():
            messages.error(request, _('Cannot delete user associated with tasks'))
            return redirect('users_list')

        messages.success(request, _('User deleted successfully'))
        return super().post(request, *args, **kwargs)

class UserLoginView(LoginView):
    template_name = 'users/login.html'

class UserLogoutView(LogoutView):
    next_page = '/'
