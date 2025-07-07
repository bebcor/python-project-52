import django_filters
from django import forms
from .models import Task
from statuses.models import Status
from django.contrib.auth import get_user_model
from labels.models import Label

User = get_user_model()

class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label='Статус',
        empty_label='Любой статус',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        label='Исполнитель',
        empty_label='Любой исполнитель',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label='Метка',
        empty_label='Любая метка',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

