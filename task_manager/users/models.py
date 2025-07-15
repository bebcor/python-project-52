from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    first_name = models.CharField(_('First Name'), max_length=150, blank=False)
    last_name = models.CharField(_('Last Name'), max_length=150, blank=False)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
