from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
        }