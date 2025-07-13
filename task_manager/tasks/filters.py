import django_filters
from django import forms
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from django.contrib.auth import get_user_model
from task_manager.labels.models import Label
import logging

logger = logging.getLogger(__name__)
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
    widget=forms.Select(attrs={
        'class': 'form-select',
        'id': 'executor-filter'})
    )

    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label='Метка',
        empty_label='Любая метка',
        widget=forms.Select(attrs={'class': 'form-select'}),
        field_name='labels__id',
        method='filter_labels'
    )
    self_tasks = django_filters.BooleanFilter(
        method='filter_self_tasks',
        label='Только мои задачи',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        required=False
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']

    def __init__(self, *args, **kwargs):
        self.request_user = kwargs.pop('request_user', None)
        super().__init__(*args, **kwargs)

    def filter_labels(self, queryset, name, value):
        logger.info(f"Фильтр меток: value={value}")
        if value:
            return queryset.filter(labels=value)
        return queryset

    def filter_self_tasks(self, queryset, name, value):
        logger.info(f"Фильтр 'Только мои задачи': value={value}, request={self.request}, user={self.request.user if self.request else 'None'}")
        if value and self.request and self.request.user.is_authenticated:
            logger.info(f"Применяю фильтр для пользователя: {self.request.user}")
            return queryset.filter(author=self.request.user)
        return queryset
