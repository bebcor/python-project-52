from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        label=_('First Name'),
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': _('First Name'),
            'id': 'first-name-field' 
        })
    )
    last_name = forms.CharField(
        label=_('Last Name'),
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': _('Last Name'),
            'id': 'last-name-field'  
        })
    )
    username = forms.CharField(
        label=_('Username'),
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': _('Username'),
            'id': 'username-field'  
        })
    )
    password1 = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': _('Password'),
            'id': 'password1-field'  
        }),
    )
    password2 = forms.CharField(
        label=_('Password confirmation'),
        widget=forms.PasswordInput(attrs={
            'placeholder': _('Password confirmation'),
            'id': 'password2-field'  
        }),
        strip=False,
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
        }
