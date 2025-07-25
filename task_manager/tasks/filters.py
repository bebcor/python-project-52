import logging

import django_filters
from django import forms
from django.contrib.auth import get_user_model

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task

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
        'id': 'id_executor_filter'})
    )
    labels = django_filters.ModelChoiceFilter(
    queryset=Label.objects.all(),
    label='Метка',
    empty_label='Любая метка',
    widget=forms.Select(attrs={'class': 'form-select'}),
    field_name='labels',
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
    
        self.filters['executor'].field.label_from_instance = \
            lambda obj: f"{obj.first_name} {obj.last_name}"

    def filter_labels(self, queryset, name, value):
        logger.info(f"Фильтр меток: value={value}")
        if value:
            return queryset.filter(labels=value)
        return queryset

    def filter_self_tasks(self, queryset, name, value):
        logger.info(
            f"Фильтр 'Только мои задачи': value={value}, "
            f"request={self.request}, "
            f"user={self.request.user if self.request else 'None'}"
        )
        if value and self.request and self.request.user.is_authenticated:
            logger.info(
                f"Применяю фильтр для пользователя: {self.request.user}"
            )
            return queryset.filter(author=self.request.user)
        return queryset
